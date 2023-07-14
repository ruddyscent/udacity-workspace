import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger


def split(source: str, destination: str) -> None:
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    source_files = glob.glob(os.path.join(source, '*.tfrecord'))
    source_files = [os.path.basename(file) for file in source_files]
    random.shuffle(source_files)

    train_files, val_files, test_files = np.split(source_files, [int(len(source_files) * 0.8), int(len(source_files) * 0.9)])

    for file in train_files:
        os.makedirs(os.path.join(destination, 'train'), exist_ok=True)
        os.rename(os.path.join(source, file), os.path.join(destination, 'train', file))

    for file in val_files:
        os.makedirs(os.path.join(destination, 'val'), exist_ok=True)
        os.rename(os.path.join(source, file), os.path.join(destination, 'val', file))

    for file in test_files:
        os.makedirs(os.path.join(destination, 'test'), exist_ok=True)
        os.rename(os.path.join(source, file), os.path.join(destination, 'test', file))
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)