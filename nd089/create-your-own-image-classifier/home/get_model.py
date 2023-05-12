#!/usr/bin/env python3

from typing import NoReturn

import torch
import torchvision

def get_model(arch: str, hidden_size: int, output_size: int) -> torch.nn.Module:
    if arch == 'vgg':
        model = torchvision.models.vgg.vgg11(pretrained=True)
        model.arch = 'vgg'
        in_features = model.classifier[0].in_features
    elif arch == 'resnet':
        model = torchvision.models.resnet.resnet18(pretrained=True)
        model.arch = 'resnet'
        in_features = model.fc.in_features
    elif arch == 'alexnet':
        model = torchvision.models.alexnet(pretrained=True)
        model.arch = 'alexnet'
        in_features = model.classifier[1].in_features
    else:
        raise Exception
    
    model.hidden_size = hidden_size
    model.output_size = output_size

    for params in model.parameters():
        params.requries_grad = False

    classifier = torch.nn.Sequential(
        torch.nn.Linear(in_features, hidden_size, bias=True),
        torch.nn.ReLU(inplace=True),
        torch.nn.Dropout(p=0.5),
        torch.nn.Linear(hidden_size, hidden_size, bias=True),
        torch.nn.ReLU(inplace=True),
        torch.nn.Dropout(p=0.5),
        torch.nn.Linear(hidden_size, output_size, bias=True),
#             torch.nn.LogSoftmax(dim=1),
    )

    if arch == 'vgg':
        model.classifier = classifier
    elif arch == 'resnet':
        model.fc = classifier
    elif arch == 'alexnet':
        model.classifier = classifier
    else:
        raise Exception

    return model

def read_model(checkpoint: str) -> torch.nn.Module:   
    checkpoint = torch.load(checkpoint)

    model = get_model(checkpoint['arch'], checkpoint['hidden_size'], checkpoint['output_size'])
    model.load_state_dict(checkpoint['state_dict'])
    
    return model, checkpoint['class_to_idx']
                
def save_model(model: torch.nn.Module, class_to_idx: dict, save_dir: str) -> NoReturn:
    checkpoint = {
        'output_size': model.output_size,
        'hidden_size': model.hidden_size,
        'state_dict': model.state_dict(),
        'arch' : model.arch,
        'class_to_idx': class_to_idx,
        }

    torch.save(checkpoint, save_dir)