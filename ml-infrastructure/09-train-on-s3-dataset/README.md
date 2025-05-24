
# 09 – Train on S3 Dataset

<img src="../../media/machine-learning.jpg" style="width: 300px" align="right">

> Move your training dataset to S3 and modify your code to load it from object storage instead of local disk — just like in cloud pipelines.

Upload your dataset to MinIO and modify your training script to load data from S3. You will now train your model without touching local disk, mimicking how training pipelines work in scalable cloud environments.

Bonus: add some versioning, like timestamps, in the filenames.

### Bonus Exercise

#### Extend the Dataset

<img src="../../media/photography-extend-dataset.jpg" style="width: 300px" align="right">

> Upload new images and labels through the frontend to expand your dataset. Add a new class, retrain your model, and re-evaluate performance.

Extend your frontend to allow uploading new images from your phone or computer to your MinIO bucket. Add a new category (e.g. keyboard, monitor) to the dataset, retrain your model, and evaluate its performance.

- Write plotly dash code to allow uploading new images
- Configure it to work with your S3 minio server
- Add a new category to the dataset and upload some images
- Retrain your model to support the new category
