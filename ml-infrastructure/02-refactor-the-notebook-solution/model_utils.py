from torchvision.models import mobilenet_v3_small, MobileNet_V3_Small_Weights
import torch.nn as nn
import torch

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def create_model(num_classes):
    """ Create a pretrained MobilenetV3 model. """
    model = mobilenet_v3_small(weights=MobileNet_V3_Small_Weights.DEFAULT)
    model.classifier[3] = nn.Linear(model.classifier[3].in_features, num_classes)
    return model.to(DEVICE)

def load_model(path="model.pth"):
    """ Load model from disk. """
    return torch.load(path).to(DEVICE)

def save_model(model, path="model.pth"):
    """ Save model to disk. """
    torch.save(model, path)
