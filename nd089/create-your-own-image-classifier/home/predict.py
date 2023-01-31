#!/usr/bin/env python3
#
# PROGRAMMER: Kyungwon Chun
# DATE CREATED: Sep. 20, 2022
# REVISED DATE: 
# PURPOSE: 
#
# <> indicates expected user input:
#      python predict.py <path_to_image> checkpoint --top_k <top_k> 
#             --category_names <category_json> --gpu
# Example call:
#     python predict.py flowers/test/1/image_06743.jpg ~/opt/best_model.pth
#             --top_k 3 --category_names cat_to_name.json --gpu    
##


from time import time

import torch
from PIL import Image

from get_input_args import get_predict_input_args
from get_model import read_model
from process_image import read_image
from train_model import inference


def main():
    in_arg = get_predict_input_args()

#     device = torch.device(
#         'cuda' if in_arg.gpu and torch.cuda.is_available() else 'cpu'
#     )
    
#     model = torch.load(in_arg.checkpoint)
#     model.eval()
#     model.to(device)

    model = read_model(in_arg.checkpoint, in_arg.gpu)
    
#     with Image.open(in_arg.image_path) as im:
#         np_image = process_image(im)
#         tensor_image = torch.tensor(np_image, dtype=torch.float)
#         tensor_image = tensor_image.unsqueeze(0).to(device)
    
    tensor_image = read_image(in_arg.image_path, in_arg.gpu)
    
    ind, prob = inference(model, tensor_image, in_arg.top_k, in_arg.category_names)
    print(f"top-k candidates: {ind}")
    print(f"top-k confidence: {prob}")
    

if __name__ == "__main__":
    main()