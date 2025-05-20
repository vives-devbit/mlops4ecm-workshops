from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from data_utils import get_classes, GroceryDataset, VAL_CSV, transform
from model_utils import load_model, DEVICE
from s3_utils import download_from_s3
import torch
import random
from io import BytesIO
from PIL import Image

app = FastAPI(title="Grocery Classifier API")

# 🧠 These are preloaded once at startup
class_names = get_classes()

# TODO download model from S3
# -> see download_from_s3()

model = load_model(num_classes=len(class_names))
model.eval()

# Dataset without transforms (we want raw images here)
val_dataset = GroceryDataset(VAL_CSV, transform=None)

@app.get("/class-names")
def get_class_names():
    """✅ Return a list of all class names."""
    # Hint: class_names is a dictionary {index: name}
    # You need to return: {"classes": [...]}
    return {"classes": list(class_names.values())}


@app.get("/random-image")
def get_random_image():
    """Return a random image from the validation set."""
    index = random.randint(0, len(val_dataset) - 1)
    image, _ = val_dataset[index]  # This is a PIL.Image

    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/jpeg")


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """This endpoint is fully implemented — it accepts an uploaded image and returns the predicted class."""
    image_data = await file.read()
    try:
        image = Image.open(BytesIO(image_data)).convert("RGB")
    except Exception:
        return JSONResponse(status_code=400, content={"error": "Invalid image format"})

    input_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor.to(DEVICE))
        _, predicted_idx = torch.max(output, 1)
        predicted_class = class_names[predicted_idx.item()]

    return {"prediction": predicted_class}

