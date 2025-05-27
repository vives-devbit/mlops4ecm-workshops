FROM python:3.11

WORKDIR /app

# Clone the dataset early (rarely changes, cacheable)
RUN git clone --depth 1 \
    https://github.com/marcusklasson/GroceryStoreDataset.git \
    /root/GroceryStoreDataset/

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app code into the container
COPY . .

# Don't store any models, they must come from S3
RUN rm -f *.pth

# Document the port used by backend
EXPOSE 8000

# Run FastAPI server (with 'run' for production server)
CMD ["fastapi", "run", "backend.py", "--host", "0.0.0.0"]

