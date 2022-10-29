import torch
import torch.nn as nn
import torch.nn.functional as F


# # define the CNN architecture
# class MyModel(nn.Module):
#     def __init__(self, num_classes: int = 1000, dropout: float = 0.7) -> None:

#         super().__init__()

#         # YOUR CODE HERE
#         # Define a CNN architecture. Remember to use the variable num_classes
#         # to size appropriately the output of your classifier, and if you use
#         # the Dropout layer, use the variable "dropout" to indicate how much
#         # to use (like nn.Dropout(p=dropout))

#         self.conv1 = nn.Conv2d(3, 12, 3, padding=1)
#         self.bn1 = nn.BatchNorm2d(12)
#         self.conv1_1 = nn.Conv2d(12, 12, 3, padding=1)
#         self.bn1_1 = nn.BatchNorm2d(12)
#         self.conv2 = nn.Conv2d(12, 48, 3, padding=1)
#         self.bn2 = nn.BatchNorm2d(48)
#         self.conv3 = nn.Conv2d(48, 192, 3, padding=1)
#         self.bn3 = nn.BatchNorm2d(192)
#         self.conv4 = nn.Conv2d(192, 768, 3, padding=1)
#         self.bn4 = nn.BatchNorm2d(768)
#         self.conv5 = nn.Conv2d(768, 1024, 3, padding=1)
#         self.bn5 = nn.BatchNorm2d(1024)

#         self.pool = nn.MaxPool2d(2, 2)
#         self.dropout = nn.Dropout(p=dropout)
        
#         self.fc1 = nn.Linear(1024*7*7, 2**10)
#         self.bn6 = nn.BatchNorm1d(2**10)
#         self.fc2 = nn.Linear(1024, 512)
#         self.bn7 = nn.BatchNorm1d(512)
#         self.fc3 = nn.Linear(512, num_classes)

#     def forward(self, x: torch.Tensor) -> torch.Tensor:
#         # YOUR CODE HERE: process the input tensor through the
#         # feature extractor, the pooling and the final linear
#         # layers (if appropriate for the architecture chosen)
        
#         x = self.pool(F.relu(self.bn1_1(self.conv1_1(
#                 F.relu(self.bn1(self.conv1(x)))
#                 )))) # (3x224x224) -> (12x112x112)
#         x = self.pool(F.relu(self.bn2(self.conv2(x)))) # (12x224x224) -> (48x56x56)
#         x = self.pool(F.relu(self.bn3(self.conv3(x)))) # (48x56x56) -> (192x28x28)
#         x = self.pool(F.relu(self.bn4(self.conv4(x)))) # (192x28x28) -> (768x14x14)
#         x = self.pool(F.relu(self.bn5(self.conv5(x)))) # (768x14x14) -> (3072x7x7)
#         x = self.dropout(x)
#         x = torch.flatten(x, 1) # flatten all dimensions except batch
#         x = F.relu(self.bn6(self.fc1(x)))
#         x = F.relu(self.bn7(self.fc2(x)))
#         x = self.fc3(x)
#         return x


# define the CNN architecture (48%)
class MyModel(nn.Module):
    def __init__(self, num_classes: int = 1000, dropout: float = 0.7) -> None:

        super().__init__()

        # YOUR CODE HERE
        # Define a CNN architecture. Remember to use the variable num_classes
        # to size appropriately the output of your classifier, and if you use
        # the Dropout layer, use the variable "dropout" to indicate how much
        # to use (like nn.Dropout(p=dropout))

        self.conv1 = nn.Conv2d(3, 12, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(12)
        self.conv2 = nn.Conv2d(12, 48, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(48)
        self.conv3 = nn.Conv2d(48, 192, 3, padding=1)
        self.bn3 = nn.BatchNorm2d(192)
        self.conv4 = nn.Conv2d(192, 768, 3, padding=1)
        self.bn4 = nn.BatchNorm2d(768)
        self.conv5 = nn.Conv2d(768, 3072, 3, padding=1)
        self.bn5 = nn.BatchNorm2d(3072)

        self.pool = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(p=dropout)
        
        self.fc1 = nn.Linear(3072*7*7, 2**10)
        self.bn6 = nn.BatchNorm1d(2**10)
        self.fc2 = nn.Linear(1024, 512)
        self.bn7 = nn.BatchNorm1d(512)
        self.fc3 = nn.Linear(512, num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # YOUR CODE HERE: process the input tensor through the
        # feature extractor, the pooling and the final linear
        # layers (if appropriate for the architecture chosen)
        
        x = self.pool(F.relu(self.bn1(self.conv1(x)))) # (3x224x224) -> (12x112x112)
        x = self.pool(F.relu(self.bn2(self.conv2(x)))) # (12x224x224) -> (48x56x56)
        x = self.pool(F.relu(self.bn3(self.conv3(x)))) # (48x56x56) -> (192x28x28)
        x = self.pool(F.relu(self.bn4(self.conv4(x)))) # (192x28x28) -> (768x14x14)
        x = self.pool(F.relu(self.bn5(self.conv5(x)))) # (768x14x14) -> (3072x7x7)
        x = self.dropout(x)
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = F.relu(self.bn6(self.fc1(x)))
        x = F.relu(self.bn7(self.fc2(x)))
        x = self.fc3(x)
        return x


# define the CNN architecture (10%)
# class MyModel(nn.Module):
#     def __init__(self, num_classes: int = 1000, dropout: float = 0.7) -> None:

#         super().__init__()

#         # YOUR CODE HERE
#         # Define a CNN architecture. Remember to use the variable num_classes
#         # to size appropriately the output of your classifier, and if you use
#         # the Dropout layer, use the variable "dropout" to indicate how much
#         # to use (like nn.Dropout(p=dropout))

#         self.conv1 = nn.Conv2d(3, 12, 3, padding=1)
#         self.bn1 = nn.BatchNorm2d(12)
#         self.conv2 = nn.Conv2d(12, 48, 3, padding=1)
#         self.bn2 = nn.BatchNorm2d(48)
#         self.conv3 = nn.Conv2d(48, 192, 3, padding=1)
#         self.bn3 = nn.BatchNorm2d(192)

#         self.pool = nn.MaxPool2d(2, 2)
#         self.dropout = nn.Dropout(p=dropout)
        
#         self.fc1 = nn.Linear(192 * 28 * 28, 2**10)
#         self.bn6 = nn.BatchNorm1d(2**10)

#         self.fc2 = nn.Linear(2**10, num_classes)

#     def forward(self, x: torch.Tensor) -> torch.Tensor:
#         # YOUR CODE HERE: process the input tensor through the
#         # feature extractor, the pooling and the final linear
#         # layers (if appropriate for the architecture chosen)
        
#         x = self.pool(F.relu(self.bn1(self.conv1(x))))
#         x = self.pool(F.relu(self.bn2(self.conv2(x))))
#         x = self.pool(F.relu(self.bn3(self.conv3(x))))
#         x = self.dropout(x)
#         x = torch.flatten(x, 1) # flatten all dimensions except batch
#         x = F.relu(self.bn6(self.fc1(x)))
#         x = self.fc2(x)
#         return x


# # define the CNN architecture (6%)
# class MyModel(nn.Module):
#     def __init__(self, num_classes: int = 1000, dropout: float = 0.7) -> None:

#         super().__init__()

#         # YOUR CODE HERE
#         # Define a CNN architecture. Remember to use the variable num_classes
#         # to size appropriately the output of your classifier, and if you use
#         # the Dropout layer, use the variable "dropout" to indicate how much
#         # to use (like nn.Dropout(p=dropout))

#         # self.conv1 = nn.Conv2d(3, 12, 3, padding=1)
#         # self.bn1 = nn.BatchNorm2d(12)
#         # self.conv2 = nn.Conv2d(12, 48, 3, padding=1)
#         # self.bn2 = nn.BatchNorm2d(48)
#         # self.conv3 = nn.Conv2d(48, 192, 3, padding=1)
#         # self.bn3 = nn.BatchNorm2d(192)
        
#         self.conv1 = nn.Conv2d(3, 9, 3, padding=1)
#         self.bn1 = nn.BatchNorm2d(9)
#         self.conv2 = nn.Conv2d(9, 27, 3, padding=1)
#         self.bn2 = nn.BatchNorm2d(27)
#         self.conv3 = nn.Conv2d(27, 81, 3, padding=1)
#         self.bn3 = nn.BatchNorm2d(81)
#         self.conv4 = nn.Conv2d(81, 723, 3, padding=1)
#         self.bn4 = nn.BatchNorm2d(723)
#         self.conv5 = nn.Conv2d(723, 2169, 3, padding=1)
#         self.bn5 = nn.BatchNorm2d(2169)

#         self.gap = nn.AdaptiveAvgPool2d((1, 1))

#         # self.conv2 = nn.Conv2d(6, 12, 3, padding=1)
#         # self.conv3 = nn.Conv2d(12, 24, 3, padding=1)
#         # self.conv4 = nn.Conv2d(24, 48, 3, padding=1)
#         # self.conv5 = nn.Conv2d(48, 96, 3, padding=1)
#         # self.bn = nn.BatchNorm2d(1024)
#         self.pool = nn.MaxPool2d(2, 2)
#         self.dropout = nn.Dropout(p=dropout)
#         # self.fc1 = nn.Linear(192 * 28 * 28, 2**10)
#         self.fc1 = nn.Linear(2169, 1024)
#         self.bn6 = nn.BatchNorm1d(2**10)
#         # self.fc1 = nn.Linear(1024, 256)
#         self.fc2 = nn.Linear(1024, num_classes)
#         # self.fc2 = nn.Linear(2**12, num_classes)
#         # self.fc2 = nn.Linear(256, num_classes)

#     def forward(self, x: torch.Tensor) -> torch.Tensor:
#         # YOUR CODE HERE: process the input tensor through the
#         # feature extractor, the pooling and the final linear
#         # layers (if appropriate for the architecture chosen)
        
#         x = self.pool(F.relu(self.bn1(self.conv1(x))))
#         x = self.pool(F.relu(self.bn2(self.conv2(x))))
#         x = self.pool(F.relu(self.bn3(self.conv3(x))))
#         x = self.pool(F.relu(self.bn4(self.conv4(x))))
#         x = self.pool(F.relu(self.bn5(self.conv5(x))))
#         x = self.gap(x)
#         # x = self.pool(F.relu(self.conv1(x)))
#         # x = self.pool(F.relu(self.conv2(x)))
#         # x = self.pool(F.relu(self.conv3(x)))
#         # x = self.pool(F.relu(self.conv4(x)))
#         # x = self.pool(F.relu(self.conv5(x)))
#         x = self.dropout(x)
#         x = torch.flatten(x, 1) # flatten all dimensions except batch
#         x = F.relu(self.bn6(self.fc1(x)))
#         x = self.fc2(x)
#         return x


######################################################################################
#                                     TESTS
######################################################################################
import pytest


@pytest.fixture(scope="session")
def data_loaders():
    from .data import get_data_loaders

    return get_data_loaders(batch_size=2)


def test_model_construction(data_loaders):

    model = MyModel(num_classes=23, dropout=0.3)

    dataiter = iter(data_loaders["train"])
    images, labels = dataiter.next()

    out = model(images)

    assert isinstance(
        out, torch.Tensor
    ), "The output of the .forward method should be a Tensor of size ([batch_size], [n_classes])"

    assert out.shape == torch.Size(
        [2, 23]
    ), f"Expected an output tensor of size (2, 23), got {out.shape}"
