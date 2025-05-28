from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import pandas as pd
import os

DATA_DIR = os.path.expanduser('~/GroceryStoreDataset/dataset')
CLASSES_CSV = os.path.join(DATA_DIR, 'classes.csv')
TRAIN_CSV = os.path.join(DATA_DIR, 'train.txt')
VAL_CSV = os.path.join(DATA_DIR, 'val.txt')
SYNTHETIC_DIR = './synthetic'

def load_synthetic_images():
    """Scan synthetic/ folder and return list of (path, label) entries."""
    synthetic_samples = []

    if not os.path.exists(SYNTHETIC_DIR):
        return synthetic_samples  # no synthetic data yet

    for label in os.listdir(SYNTHETIC_DIR):
        label_dir = os.path.join(SYNTHETIC_DIR, label)
        if not os.path.isdir(label_dir):
            continue
        for filename in os.listdir(label_dir):
            if filename.lower().endswith((".jpg", ".png")):
                full_path = os.path.join(label_dir, filename)
                synthetic_samples.append((full_path, label))

    return synthetic_samples

class GroceryDataset(Dataset):
    def __init__(self, csv_file, transform=None, extra_data=None):
        self.df = pd.read_csv(csv_file, header=None)
        self.df.columns = ["path", "fine_label", "coarse_label"]

        self.samples = [
            (os.path.join(DATA_DIR, row["path"]), row["coarse_label"])
            for _, row in self.df.iterrows()
        ]

        if extra_data:
            class_name_to_id = {
                v: k for k, v in get_classes().items()
            }
            for path, class_name in extra_data:
                if class_name in class_name_to_id:
                    self.samples.append((path, class_name_to_id[class_name]))

        self.transform = transform

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        path, label = self.samples[idx]
        image = Image.open(path).convert("RGB")
        if self.transform:
            image = self.transform(image)
        return image, label

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

def get_classes():
    """ Load class names. Returns dict(int => class name) """
    return (
        pd.read_csv(CLASSES_CSV)
        .drop_duplicates("Coarse Class ID (int)")
        .set_index("Coarse Class ID (int)")["Coarse Class Name (str)"]
        .to_dict()
    )

def get_loaders(batch_size=32, include_synthetic=False):
    """ Get train and validation dataloaders. """
    synthetic_data = load_synthetic_images() if include_synthetic else None

    train_dataset = GroceryDataset(TRAIN_CSV, transform=transform, extra_data=synthetic_data)
    val_dataset = GroceryDataset(VAL_CSV, transform=transform)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=True)
    return train_loader, val_loader
