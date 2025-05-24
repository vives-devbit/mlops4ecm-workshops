from torchvision.models import mobilenet_v3_small, MobileNet_V3_Small_Weights
import torch.nn as nn
import torch

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def create_model(num_classes):
    """Create a pretrained MobileNetV3 model with a custom classifier."""
    model = mobilenet_v3_small(weights=MobileNet_V3_Small_Weights.DEFAULT)
    model.classifier[3] = nn.Linear(model.classifier[3].in_features, num_classes)
    return model.to(DEVICE)

def save_model(model, path="model.pth"):
    """Save model weights (state dict) to disk."""
    torch.save(model.state_dict(), path)

def load_model(num_classes, path="model.pth"):
    """Create model and load weights from disk."""
    model = create_model(num_classes)
    model.load_state_dict(torch.load(path, map_location=DEVICE))
    return model
