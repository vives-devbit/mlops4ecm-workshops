import torch.optim as optim
import torch.nn as nn
import torch
from .model_utils import DEVICE
from tqdm import tqdm

def train_model(model, dataloader, epochs=5, learning_rate=1e-3):
    """ Trains the model for a number of epochs. """
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Training loop
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for images, labels in tqdm(dataloader, desc=f"Epoch {epoch+1}"):
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * images.size(0)
        print(f"Epoch {epoch+1} - Loss: {total_loss / len(dataloader.dataset):.4f}")


def evaluate_model(model, dataloader):
    """ Returns model accuracy. """
    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in dataloader:
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)

    return correct / total
