"""
Image Classifier Prediction Script

This script takes an input image and a trained model, and predicts the top-k classes for the image using the model.

Author: Kyugwon Chun
Date: Tue. March 19, 2024
"""

import argparse
import json
import logging
from typing import List, Tuple, Union
import numpy as np
import tensorflow as tf

from PIL import Image
from tensorflow_hub import KerasLayer

logger = tf.get_logger()
logger.setLevel(logging.ERROR)

image_size = 224

def process_image(image: tf.Tensor) -> np.ndarray:
    """
    Preprocesses the input image tensor.

    Args:
        image (tf.Tensor): The input image tensor.

    Returns:
        np.ndarray: The preprocessed image as a NumPy array.
    """
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, (image_size, image_size))
    image /= 255
    return image.numpy()

def predict(image: np.ndarray, model: tf.keras.Model, class_names: dict = None, top_k: int = 5) -> Tuple[List[float], List[Union[str, int]]]:
    """
    Predicts the top-k classes for a given image using a trained model.

    Args:
        image (np.ndarray): The input image to be classified.
        model (tf.keras.Model): The trained model used for prediction.
        class_names (dict, optional): A dictionary mapping class indices to class names. Defaults to None.
        top_k (int, optional): The number of top classes to return. Defaults to 5.

    Returns:
        Tuple[List[float], List[Union[str, int]]]: A tuple containing two lists:
            - The top-k probability values for each predicted class.
            - The top-k class names or indices, depending on whether class_names is provided.
    """
    ps = model.predict(image)
    top_k_values, top_k_indices = tf.nn.top_k(ps, k=top_k)
    top_k_values = top_k_values.numpy().tolist()[0]
    top_k_indices = top_k_indices.numpy().tolist()[0]
    if class_names:
        top_k_names = [class_names[index] for index in top_k_indices]
    else:
        top_k_names = top_k_indices
    return top_k_values, top_k_names

def main(args: argparse.Namespace) -> None:
    """
    Runs the main prediction process.

    Args:
        args (argparse.Namespace): The command-line arguments.

    Returns:
        None
    """
    logger.info("Starting prediction process")
    try:
        if args.category_path is None:
            class_names = None
        else:
            with open(args.category_path, 'r', encoding='utf-8') as f:
                class_names = json.load(f)
                class_names = {int(k): v for k, v in class_names.items()}

        logger.info(f"Opening image from {args.image_path}")
        im = Image.open(args.image_path)
        test_image = np.asarray(im)
        processed_test_image = process_image(test_image)
        processed_test_image = np.expand_dims(processed_test_image, axis=0)

        logger.info(f"Loading model from {args.model_path}")
        reloaded_keras_model = tf.keras.models.load_model(
            args.model_path, 
            custom_objects={'KerasLayer': KerasLayer})

        logger.info("Making prediction")
        top_k_values, top_k_names = predict(processed_test_image, reloaded_keras_model, class_names, args.top_k)
        for i in range(len(top_k_values)):
            print(f"Prediction {i+1}:")
            print(f"Class name: {top_k_names[i]}")
            print(f"Probability: {top_k_values[i]}")
            print("------------------------")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Classify image of flowers')
    parser.add_argument('image_path', type=str, help='Path to image to predict')
    parser.add_argument('model_path', type=str, help='Path to model file')
    parser.add_argument('--top_k', type=int, help='Number of top K classes to return', default=3)
    parser.add_argument('--category_path', type=str, help='Path to category names file')

    args = parser.parse_args()
    main(args)
