## Lab 08 – Deploy Model from S3

<img src="../../media/s3-minio-logos-name.jpg" style="width: 300px" align="right">

> In this lab, you'll store your trained model in S3-style object storage using **MinIO**, and make your FastAPI backend load it directly from there. This simulates how machine learning models are managed and deployed in real production environments.

You’ll be given working infrastructure and code templates — your task is to fill in just a few missing pieces. Once completed, your system will:

- ✅ Upload trained models to MinIO
- ✅ Serve them from the backend by downloading from MinIO
- ✅ Confirm the full workflow via a running frontend

### 🧭 Overview of Tasks

| Step     | Goal                       | What You’ll Fix                                              |
| -------- | -------------------------- | ------------------------------------------------------------ |
| 1        | Set up the MinIO server    | Create your `.env` file, start MinIO, create a bucket        |
| 2        | Upload the model to S3     | Complete the `upload_to_s3` and `download_from_s3` helpers   |
| 3        | Serve model from S3        | Add model download logic to `backend.py`                     |
| 🔁 Bonus | Auto-reload new models     | Implement model polling to detect when the model changes    |

### 🔧 Step 1 – Set Up the MinIO Server

In this step, you’ll launch a **local object storage server** (MinIO) that acts like AWS S3. You’ll configure it with your own credentials and access it through a web interface. Later, your training code and API will use this server to upload and download models.

#### ✅ 1. Create your `.env` file

To run the MinIO server and interact with S3 from your code, we need a few configuration values: a **username**, a **password**, the **endpoint URL** of the server, and the **bucket name** you want to use. These are called **environment variables**.

We store these values in a file named `.env` — but this file is **not included in Git**. Why?

- 🧠 Environment files like `.env` contain **secrets and machine-specific settings**. For example, your MinIO password or access keys.
- ✅ It’s **best practice** not to commit these files to version control — especially in team projects or public repositories.
- Instead, your project includes a **template** file named `.env.example`. You’ll copy that and create your own private version.

Inside the `08-deploy-model-from-s3/` folder, run:

```bash
cp .env.example .env
```

Then open the `.env` file in **Visual Studio Code** and fill in your own values:

```env
MINIO_ROOT_USER=mlops-user              # Your username for MinIO
MINIO_ROOT_PASSWORD=super-secret-pass   # Your password
MINIO_ENDPOINT_URL=http://<vm-ip>:9000  # Your VM’s IP address here!
MINIO_BUCKET=ml-models                  # The name of your S3 bucket
```

> 💡 `.env` files are **hidden on Linux** (files that start with a `.` don’t show up with `ls`), but you can see them with `ls -a`

Once this file exists, all parts of your system — the MinIO server, your training code, your API — can read these values automatically and use them to connect to S3.

#### ✅ 2. Start the MinIO server

To start MinIO, we’ll use Docker Compose — but since our file is named something other than the default `docker-compose.yml`, we need to specify it explicitly using `-f`.

Run:

```bash
docker compose -f compose-minio.yml up -d --build
```

If everything works correctly, Docker will spin up a MinIO container and print something like:

```
[+] Running 2/2
 ✔ Network 08-deploy-model-from-s3_default     Created
 ✔ Container 08-deploy-model-from-s3-minio-1   Started
```

Just **for your information**, the command to take it back down is:
```bash
# This takes the minio server back down
docker compose -f compose-minio.yml down
# Don't run this now, just for your information
```

#### ✅ 3. Visit the MinIO Web UI

Now open your browser and visit:

```
http://<your-vm-ip>:9001
```

This is the MinIO **admin console**. Log in using the username and password you set in your `.env` file.

Once logged in:

1. Click **"Buckets"** in the left menu.
2. Click **"Create Bucket"**
3. Enter your `.env` BUCKET name (e.g. `ml-models`) and click **"Create Bucket"**.

✅ Your S3-compatible object storage is now ready to use.

#### 🧪 4. Try Uploading a File

To confirm that everything works:

1. Select your bucket and click **"Upload"**.
2. Choose a simple file (e.g. a `.txt` or `.jpg`) from your computer.
3. Click **"Upload"** to send it to the bucket.

If you see the file in the bucket, your MinIO server is working correctly — and you're ready to move on to uploading your trained models.

### 📤 Step 2 – Upload the Model to MinIO from the Training Script

Your training script is already set up to call an `upload_to_s3()` function — but that function needs to be implemented.

1. Open `backend/s3_utils.py` and fix the `upload_to_s3()` function. [Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html)
2. Open the `run_training.py` script and notice this at the top (loads the .env file):
   ```python
   # Load environment variables from .env
   from dotenv import load_dotenv
   load_dotenv()
   ```
3. Install the `dotenv` library:
   ```bash
   source .venv/bin/activate
   pip install dotenv
   ```
4. Run the training script:
   ```bash
   python3 run_training.py
   ```
5. After training, check the **MinIO web UI** to verify that the model file appeared in your bucket.

### 📥 Step 3 – Download the Model in the Backend

Now that your model is stored in MinIO, the backend needs to download it at startup.

1. In `backend/backend.py`, locate the TODO for downloading the model from S3.
2. Add the line to call your `download_from_s3()` function.
3. Start the backend using Docker Compose:

   ```bash
   docker compose -f compose-app.yml up --build
   ```
4. Visit your frontend at `http://<vm-ip>:8050` and verify that predictions work.

If they do — your model was **loaded from object storage** successfully!

### 🌟 Bonus Exercise: Auto-Redeploy New Models

Add logic to **periodically check** for a newer model version in your MinIO bucket.

* Use `boto3` to get 'LastModified' of your model
* Reload the model if a newer one appears.
* Optionally run this check in a background thread.

```
response = s3.head_object(Bucket=, Key=)

last_modified = response['LastModified']
```
