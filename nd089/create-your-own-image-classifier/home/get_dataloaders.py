#!/usr/bin/env python3

import torch
import torchvision
import torchvision.transforms as T

from typing import Tuple


def get_dataloaders(data_dir: str) -> Tuple[dict, dict]:
    train_dir = data_dir + '/train'
    valid_dir = data_dir + '/valid'
    test_dir = data_dir + '/test'

    data_transforms = {
        'train': T.Compose([
            T.Resize(256),
            T.RandomRotation(degrees=(0, 180)),
            T.RandomHorizontalFlip(p=0.5),
            T.RandomVerticalFlip(p=0.5),
            T.RandomResizedCrop(size=224),
            T.ToTensor(),
            T.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ]),
        'val': T.Compose([
            T.Resize(256),
            T.CenterCrop(224),
            T.ToTensor(),
            T.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ]),
        'test': T.Compose([
            T.Resize(256),
            T.CenterCrop(224),
            T.ToTensor(),
            T.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ])
    }

    image_datasets = {
        'train': torchvision.datasets.ImageFolder(
            train_dir, transform=data_transforms['train']),
        'val': torchvision.datasets.ImageFolder(
            valid_dir, transform=data_transforms['val']),
        'test': torchvision.datasets.ImageFolder(
            test_dir, transform=data_transforms['test'])
    }

    dataloaders = {
        'train': torch.utils.data.DataLoader(
            image_datasets['train'], batch_size=128, shuffle=True, num_workers=0),
        'val': torch.utils.data.DataLoader(
            image_datasets['val'], batch_size=128, shuffle=False, num_workers=0),
        'test': torch.utils.data.DataLoader(
            image_datasets['test'], batch_size=128, shuffle=False, num_workers=0),
    }
    
    return dataloaders, image_datasets['train'].class_to_idx

