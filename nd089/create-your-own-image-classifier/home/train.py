#!/usr/bin/env python3
#
# PROGRAMMER: Kyungwon Chun
# DATE CREATED: Sep. 19, 2022
# REVISED DATE: 
# PURPOSE: Train a new network on a data set
#
# <> indicates expected user input:
#      python train.py <data_dir> --save_dir <save_directory> --arch <model>
#             --learning_rate <learning_rate> --hidden_units <hidden_units>
#             --epochs <epochs> --gpu
# Example call:
#      python train.py flowers --save_dir ~/opt --arch vgg \
#             --learning_rate 0.001 --hidden_units 4096 --epochs 30 --gpu    
##

from time import time

from get_input_args import get_train_input_args
from get_dataloaders import get_dataloaders
from get_model import get_model
from train_model import train_model


def main():
    start_time = time()
    in_arg = get_train_input_args()
    dataloaders, class_to_idx = get_dataloaders(in_arg.data_dir)
    model = get_model(in_arg.arch, in_arg.hidden_units)
    train_model(model, dataloaders, in_arg.epochs, in_arg.learning_rate, 
                in_arg.gpu, in_arg.save_dir, class_to_idx)
    end_time = time()
    
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600))) + ":" + str(int((tot_time%3600)/60)) + ":"
          + str(int((tot_time%3600)%60)))
    
    
# Call to main function to run the program
if __name__ == "__main__":
    main()
    