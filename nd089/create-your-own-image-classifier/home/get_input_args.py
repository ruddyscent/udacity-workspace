#!/usr/bin/env python3

import argparse

def get_train_input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--data_dir", type=str, default="flowers", help="Path to dataset folder")
    parser.add_argument("--save_dir", type=str, default="checkpoint.pt",
                        help="Folder to store the trained model")
    parser.add_argument("--arch", type=str, default='vgg', choices=['vgg', 'resnet', 'alexnet'],
                        help="CNN Model (vgg, resnet, alexnet) with default value vgg")
    parser.add_argument("--learning_rate", type=float, default=1e-3,
                        help="The learning rate with default value 1e-3")
    parser.add_argument("--hidden_size", type=int, default=4096,
                        help="The number of hidden units in classifier with default value 4096")
    parser.add_argument("--output_size", type=int, default=102,
                        help="The number of output units in classifier with default value 102")
    parser.add_argument("--epochs", type=int, default=20,
                        help="The number of epochs with default value 20")
    parser.add_argument("--gpu", action="store_true", default=True,
                        help="Enable GPU support")

    return parser.parse_args()


def get_predict_input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--image_path", type=str, default="flowers/test/1/image_06743.jpg", 
                        help="Path to input image")
    parser.add_argument("--checkpoint", type=str, default="checkpoint.pt",
                        help="Path to model checkpoint")
    parser.add_argument("--top_k", type=int, default=3,
                        help="Number of most likely classes to return with default value 3")
    parser.add_argument("--category_names", type=str, default="cat_to_name.json",
                        help="Path to json files which contains real categori names")
    parser.add_argument("--gpu", action="store_true", default=True,
                        help="Enable GPU support")

    return parser.parse_args()
