#!/usr/bin/env python3

import argparse

def get_train_input_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("data_dir", type=str, help="Path to dataset folder")
    parser.add_argument("--save_dir", type=str,
                        help="Folder to store the trained model")
    parser.add_argument("--arch", type=str, default='vgg',
                        help="CNN Model (vgg, resnet, alexnet) with default value vgg")
    parser.add_argument("--learning_rate", type=float, default=1e-3,
                        help="The learning rate with default value 1e-3")
    parser.add_argument("--hidden_units", type=int, default=4096,
                        help="The number of hidden units in classifier with default value 4096")
    parser.add_argument("--epochs", type=int, default=20,
                        help="The number of epochs with default value 20")
    parser.add_argument("--gpu", action="store_true", 
                        help="Enable GPU support")
    
    return parser.parse_args()


def get_predict_input_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("image_path", type=str, help="Path to input image")
    parser.add_argument("checkpoint", type=str, help="Path to model checkpoint")
    parser.add_argument("--top_k", type=int, default=3,
                        help="Number of most likely classes to return with default value 3")
    parser.add_argument("--category_names", type=str, default=None,
                        help="Path to json files which contains real categori names")
    parser.add_argument("--gpu", action="store_true", 
                        help="Enable GPU support")
    
    return parser.parse_args()
