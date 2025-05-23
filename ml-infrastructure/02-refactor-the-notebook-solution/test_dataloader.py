""" Unit tests for data_utils.py """
import torch
from data_utils import get_loaders

def test_dataloader_basic():
    train_loader, val_loader = get_loaders(batch_size=4)

    # Check that dataloaders are non-empty
    assert len(train_loader) > 0
    assert len(val_loader) > 0

    # Get one batch
    images, labels = next(iter(train_loader))

    # Check image shape
    assert images.shape == (4, 3, 224, 224)

    # Check label shape and type
    assert labels.ndim == 1
    assert labels.dtype == torch.int64  # should be long/int

    # Check image tensor dtype and range
    assert isinstance(images, torch.Tensor)
    assert images.dtype == torch.float32

