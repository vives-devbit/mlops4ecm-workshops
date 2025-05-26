## Lab 04 – Backend with FastAPI

<img src="../../media/fastapi-logo-and-name.png" style="width: 300px" align="right">

> Serve your trained model through a REST API built with FastAPI. Create an endpoint that accepts image uploads and returns predictions.

In this lab, you’ll **wrap your trained model into a REST API** using [FastAPI](https://fastapi.tiangolo.com/), a modern and fast web framework for building APIs in Python. This allows your model to be queried over HTTP — by other apps, frontends, or users.

You’ll build an API with three endpoints:

1. `GET /class-names` – return a list of class labels
2. `GET /random-image` – return a random sample image from the dataset
3. `POST /predict` – accept an image and return the model’s prediction

The third endpoint is already implemented for you. Your job is to complete the first two.

### 🧭 Step 1 – Start the FastAPI Backend

We’ve already provided a `backend.py` file inside this folder. Let’s run it.

#### ✅ Start the FastAPI dev server

In the terminal, begin by installing `fastapi`:

```bash
.venv/bin/activate
pip install fastapi[standard]
```

Once installed you need to provide your own `data_utils.py`, `model_utils.py` and `model.pth` files. Then run:

```bash
cd ml-infrastructure/04-backend-with-fastapi
fastapi dev backend.py --host 0.0.0.0
```

#### 📖 What does this command do?

* `fastapi dev` — launches the development server with auto-reload
* `backend.py` — this is the entrypoint that defines your API
* `--host 0.0.0.0` — makes the API accessible from other devices (e.g. your browser)

Once the server is running, it should print something like:

```
INFO   Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO   Started reloader process [23543] using WatchFiles
INFO   Started server process [23570]
INFO   Waiting for application startup.
INFO   Application startup complete.
```

### 🌐 Step 2 – Open the Swagger UI

Open your browser and go to:

```
http://<your-vm-ip>:8000/docs
```

This opens the **Swagger UI** — an interactive page where you can explore and test the API.

You should see three endpoints:

* `GET /class-names`
* `GET /random-image`
* `POST /predict`

Try clicking **“Try it out”** on `GET /class-names` — you’ll see it doesn’t work yet. That’s expected.

Let’s fix that.

### 🛠️ Step 3 – Complete the TODOs

Open the `backend.py` file. You’ll find two `TODO` comments for the endpoints you need to finish.

#### ✅ 1. Implement `/class-names`

This endpoint should return a list of the model's class labels.

Look at this line at the top of the file:

```python
class_names = get_classes()
```

This is a dictionary mapping integer labels to class names, like `{0: 'apple', 1: 'banana', ...}`

You need to return a JSON response like this:

```json
{ "classes": ["apple", "banana", "milk"] }
```

#### ✅ 2. Implement `/random-image`

This endpoint should return a **random image from the validation set**.

Steps:

1. Pick a random index from the `val_dataset`
2. Get the corresponding image (a `PIL.Image`) — use `val_dataset[index]`
3. Save it to an in-memory `BytesIO` buffer as JPEG
4. Return it using `StreamingResponse`

The code is almost done for you — you just need to insert the part where the image is selected.

### 🤖 Step 4 – Run a Prediction

The `POST /predict` endpoint is already complete.

In Swagger UI:

1. Click `POST /predict`
2. Click **“Try it out”**
3. Upload a sample image from the dataset (e.g. a `.jpg`)
4. Click **“Execute”**

You should see a response like:

```json
{ "prediction": "milk" }
```

Behind the scenes, the image is passed to the model, which returns the predicted class label.

### 🧠 Key Takeaways

* You now have a **fully working ML backend** that serves predictions over HTTP.
* You explored your API using **Swagger UI**, a built-in interface provided by FastAPI.
* You wrote two useful endpoints: one to list class names, and one to return a random image.

✅ In the next lab, we’ll hook this backend up to a **Dash frontend** — so users can interact with your model in the browser.

