
from datetime import datetime
from tqdm import tqdm
from typing import List, NoReturn, Tuple

import json
import os
import torch

from get_model import save_model

def train_model(
    model: torch.nn.Module,
    dataloaders: dict, 
    epochs: int, 
    learning_rate: float,
    gpu: bool,
    save_dir: str
) -> NoReturn:
    device = torch.device('cuda' if gpu and torch.cuda.is_available() else 'cpu')
            
    model.train()
    model.to(device)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    best_vloss = 1_000_000.

    loss_fn = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)

    for epoch in tqdm(range(epochs)):
        print(f"EPOCH: {epoch + 1}/{epochs}")
        avg_loss = train_one_epoch(
            model, epoch, dataloaders, optimizer, loss_fn, device)
        with torch.no_grad():
            running_vloss = 0.0
            correct = 0
            total = 0
            for i, vdata in enumerate(dataloaders['val']):
                vinputs = vdata[0].to(device)
                vlabels = vdata[1].to(device)
                voutputs = model(vinputs)
                vloss = loss_fn(voutputs, vlabels)
                running_vloss += vloss

                _, predicted = torch.max(voutputs.data, 1)
                total += vlabels.size(0)
                correct += (predicted == vlabels).sum().item()
            
            avg_vloss = running_vloss / (i + 1)
            print(f"train loss: {avg_loss:.2f}, "
                  f"valid loss: {avg_vloss:.2f}, "
                  f"valid acc: {correct / total:.2f}")

            # Track best performance, and save the model's state
            if avg_vloss < best_vloss:
                best_vloss = avg_vloss
                save_model(model, dataloaders['train'].dataset.class_to_idx, save_dir)

def train_one_epoch(model: torch.nn.Module,
                    epoch_index: int, 
                    dataloaders: dict, 
                    optimizer: torch.optim.Optimizer, 
                    loss_fn: torch.nn.Module,
                    device: torch.device) -> float:
    running_loss = 0.
    last_loss = 0.

    for i, data in enumerate(dataloaders['train']):
        # Every data instance is an input + label pair
        inputs = data[0].to(device)
        labels = data[1].to(device)
        # Zero your gradients for every batch!
        optimizer.zero_grad()
        outputs = model(inputs)
        # Compute the loss and its gradients
        loss = loss_fn(outputs, labels)
        loss.backward()
        # Adjust learning weights
        optimizer.step()
        # Gather data and report
        running_loss += loss.item()
        if i % 10 == 9:
            last_loss = running_loss / 10 # loss per batch
            # print(f"  batch {i + 1} loss: {last_loss}")
            running_loss = 0.
            
    return last_loss


def inference(model: torch.nn.Module, tensor_image: torch.Tensor, topk: int, class_to_idx: dict, category_names: str) -> Tuple[List, List]:
    with torch.no_grad():
        outputs = model(tensor_image)
        # the class with the highest energy is what we choose as prediction
        confidence = torch.nn.functional.softmax(outputs.data, dim=1)
        res, ind = torch.topk(confidence, topk, dim=1)   
        
    idx2cls = {val: key for key, val in class_to_idx.items()}
    ind = list(map(lambda x: idx2cls[x], ind.squeeze().cpu().numpy()))
    prob = res.squeeze().cpu().numpy()
 
    if category_names:
        with open(category_names, 'r') as f:
            cat_to_name = json.load(f)
            ind = list(map(lambda x: cat_to_name[x], ind))

    return ind, prob
