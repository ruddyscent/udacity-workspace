from PIL import Image
import numpy as np
import torch


def process_image(image: Image) -> np.ndarray:
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''    
    # TODO: Process a PIL image for use in a PyTorch model
    width, height = image.size
    if width > height:
        image_resized = image.resize((256 * width // height, 256))
    else:
        image_resized = image.resize((256, 256 * height // width))
    image_croped = image_resized.crop((15, 15, 15 + 224, 15 + 224))
    np_image = np.array(image_croped, dtype=float) / 255
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    np_image = (np_image - mean) / std
    np_image = np_image.transpose((2, 0, 1))
    return np_image


def read_image(image_path: str, gpu: bool) -> torch.Tensor:
    device = torch.device(
        'cuda' if gpu and torch.cuda.is_available() else 'cpu'
    )
    
    with Image.open(image_path) as im:
        np_image = process_image(im)
        tensor_image = torch.tensor(np_image, dtype=torch.float)
        tensor_image = tensor_image.unsqueeze(0).to(device)
        
    return tensor_image