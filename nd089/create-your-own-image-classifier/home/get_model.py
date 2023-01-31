#!/usr/bin/env python3

import torch
import torchvision

def get_model(arch: str, hidden_units: int) -> torch.nn.Module:
    if arch == 'vgg':
        model = torchvision.models.vgg.vgg11(pretrained=True)
    elif arch == 'resnet':
        model = torchvision.models.resnet.resnet18(pretrained=True)
    elif arch == 'alexnet':
        model = torchvision.models.alexnet(pretrained=True)
    else:
        raise Exception
        
    for params in model.parameters():
        params.requries_grad = False

    if arch == 'vgg':
        in_features = model.classifier[0].in_features
        model.classifier = torch.nn.Sequential(
            torch.nn.Linear(in_features, hidden_units, bias=True),
            torch.nn.ReLU(inplace=True),
            torch.nn.Dropout(p=0.5),
            torch.nn.Linear(hidden_units, hidden_units, bias=True),
            torch.nn.ReLU(inplace=True),
            torch.nn.Dropout(p=0.5),
            torch.nn.Linear(hidden_units, 102, bias=True),
#             torch.nn.LogSoftmax(dim=1),
        )
    elif arch == 'resnet':
        in_features = model.fc.in_features
        model.fc = torch.nn.Sequential(
            torch.nn.Linear(in_features, hidden_units, bias=True),
            torch.nn.ReLU(inplace=True),
            torch.nn.Dropout(p=0.5),
            torch.nn.Linear(hidden_units, hidden_units, bias=True),
            torch.nn.ReLU(inplace=True),
            torch.nn.Dropout(p=0.5),
            torch.nn.Linear(hidden_units, 102, bias=True),
#             torch.nn.LogSoftmax(dim=1),
        )
    elif arch == 'alexnet':
        in_features = model.classifier[1].in_features
        model.classifier = torch.nn.Sequential(
            torch.nn.Dropout(p=0.5),
            torch.nn.Linear(in_features, hidden_units, bias=True),
            torch.nn.ReLU(inplace=True),
            torch.nn.Dropout(p=0.5),
            torch.nn.Linear(hidden_units, hidden_units, bias=True),
            torch.nn.ReLU(inplace=True),
            torch.nn.Linear(hidden_units, 102, bias=True),
#             torch.nn.LogSoftmax(dim=1),
        )
    else:
        raise Exception
        
    return model


def read_model(checkpoint: str, gpu: bool) -> torch.nn.Module:
    device = torch.device(
        'cuda' if gpu and torch.cuda.is_available() else 'cpu'
    )
    
    model = torch.load(checkpoint)
    model.eval()
    model.to(device)
    return model