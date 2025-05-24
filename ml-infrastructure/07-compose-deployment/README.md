
## Lab 07 – Compose Deployment

<img src="../../media/docker-compose-octopus.jpg" style="width: 300px" align="right">

> In this lab, you’ll use Docker Compose to launch your entire application — both the FastAPI backend and the Dash frontend — with a **single command**. After that, you’ll deploy the full project to a **production VM** using GitHub.

### 🧱 Part 1 – Local Compose Setup

#### 🎯 Goal

Run your full machine learning application **locally**, using a single command:

```bash
docker compose up
```

By the end of this section, both your backend (model API) and frontend (user interface) will be running in containers — networked together automatically, with no manual container juggling.

#### 🗂️ What’s Already Provided?

This folder includes a ready-to-use `docker-compose.yml` file. It defines **two services**: one for the backend, one for the frontend.

```yaml
services:
  backend:
    build: ./backend
    container_name: grocery-backend
    ports:
      - "8000:8000"
    restart: always

  frontend:
    build: ./frontend
    container_name: grocery-frontend
    ports:
      - "8050:8050"
    restart: always
```

This Compose file does a few important things:

* Builds each container from its own `Dockerfile` (`./backend`, `./frontend`)
* Exposes the backend on port **8000** (FastAPI + Swagger UI)
* Exposes the frontend on port **8050** (Dash web app)
* Uses `restart: always` so that both services will **automatically restart** after a crash or system reboot — just like in production

> 💡 Docker Compose automatically creates a private network where containers can talk to each other by name (e.g. `http://backend:8000`), so you don’t need to configure that manually.

#### 🛠️ Add Your Application Code

Before running anything, you need to **copy your existing application code** into the correct subfolders:

| Your File        | Paste into this folder            |
| ---------------- | --------------------------------- |
| `backend.py`     | `07-compose-deployment/backend/`  |
| `model_utils.py` | `07-compose-deployment/backend/`  |
| `data_utils.py`  | `07-compose-deployment/backend/`  |
| `model.pth`      | `07-compose-deployment/backend/`  |
| `frontend.py`    | `07-compose-deployment/frontend/` |

Make sure the required files are in place before proceeding.

#### ▶️ Build and Run the Application

From the `07-compose-deployment` folder, run:

```bash
docker compose up -d
```

This command:

* Builds Docker images for the backend and frontend (if needed)
* Starts both containers in the background (`-d` = detached mode)
* Automatically connects them to the same internal network
* Maps the correct ports to your VM so you can access them in a browser

> 🧠 Tip: The `docker-compose.yml` becomes your **one-stop definition** for running the entire system. No more remembering long `docker run` commands!

#### 🌐 Test the Application

Once the containers are running:

1. Open your browser and visit:
   `http://<your-vm-ip>:8050`
   → You should see the Dash interface.

2. Click **"Predict random image"**
   → It should load an image and display a prediction — meaning the frontend and backend are talking to each other.

3. To access the FastAPI docs, go to:
   `http://<your-vm-ip>:8000/docs`
   → This is the Swagger UI automatically provided by FastAPI.

#### 🔍 Useful Docker Compose Commands

Here are some handy commands for managing your project with Compose:

```bash
docker compose up --build   # Rebuild images and start services
docker compose down         # Stop and remove all containers
docker compose logs         # Show logs from both containers
docker compose restart      # Restart all services
docker ps                   # Show currently running containers
```

> 🔁 If you make code changes, use `docker compose up --build` to rebuild the images.

### 🚀 Part 2 – Set up GitHub and Push Your Code

<img src="../../media/github-logo-name.png" style="width: 300px" align="right">

In this step, you’ll publish your application code to **GitHub** so it can be cloned and deployed on your production VM.

#### ✅ Step 1 – Create a GitHub Account (if needed)

If you don’t have a GitHub account yet:

1. Go to [https://github.com/join](https://github.com/join)
2. Follow the steps to create your account — it’s free.

#### ✅ Step 2 – Create a New Repository

Once you’re logged in:

1. Click the **+** icon in the top-right corner → **"New repository"**
2. Name it something like `grocery-store`
3. Choose **public** (easier for this workshop)
4. Click **"Create repository"**

Don’t initialize it with a README or `.gitignore` — we’ll add files manually.

#### ✅ Step 3 – Generate a Fine-Grained Personal Access Token

This token will let Git push to your repository securely.

1. Go to **Settings → Developer settings → Personal access tokens → Tokens (fine-grained)**
2. Click **"Generate new token"**
3. Name it something like `"MLOps Workshop"`
4. Under **Repository access**, choose **Only select repositories** → pick your new repo
5. Under **Permissions**, set:

   * **Repository contents** → **Read and write**
6. Click **"Generate token"**

> 🔐 Copy and save the token now — you won’t be able to see it again.

#### ✅ Step 4 – Authenticate Git Using Your Token

Any time Git asks for credentials:

* Use your **GitHub username** as the username
* Use your **personal access token** as the password

This applies to `git clone`, `git push`, etc.

#### ✅ Step 5 – Configure Git Locally

To avoid repeated prompts and make Git commits traceable, run:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --global credential.helper store
```

This stores your token in a plain-text file (`~/.git-credentials`). For this workshop context — and with a limited-scope token — that's perfectly fine.

#### ✅ Step 6 – Clone Your Repository

Now it's time to clone the repo on your virtual machine:

```bash
git clone https://github.com/your-username/grocery-store.git
cd grocery-store/
```

#### ✅ Step 7 – Copy and Push Your Code

Now copy in your working application code:

```bash
cp -r ~/<date>-mlops-workshops/ml-infrastructure/07-compose-deployment/* .
```

Then commit and push:

```bash
git add .
git commit -m "First commit of grocery store repo"
git push -u origin main
```

✅ That’s it — your code is now live on GitHub and ready for deployment.

### 💻 Part 3 – Deploy to the Production VM

<img src="../../media/deployment-server.png" style="width: 300px" align="right">

Up to this point, you've been working entirely on your **development virtual machine** — the first VM you received, where you trained your model, built your API, and tested everything locally.

Now it’s time to simulate a **real deployment**.

You’ll receive access to a second VM — the **production virtual machine** — where you’ll deploy your app just like you would in a real-world scenario.

#### 🧾 Step 1 – Connect to the Production VM

Your instructor will give you the IP address and login credentials for the production VM.

You can connect in two ways:

* **Via VS Code** (just like with the development VM), using the “Remote SSH” feature
* **Or via the terminal**, using a standard SSH command:

```bash
ssh root@<production-vm-ip>
```

#### 📦 Step 2 – Clone Your GitHub Repository

Once connected to the production VM, clone your application code.

You **don’t need authentication** because your repository is public:

```bash
git clone https://github.com/YOUR_USERNAME/grocery-store.git
cd grocery-store
```

This gives you a local copy of your entire project — including the Dockerfiles and `docker-compose.yml`.

#### ▶️ Step 3 – Start the Application with Docker Compose

Now start everything using:

```bash
docker compose up -d
```

This single command will:

* Build the backend and frontend containers
* Start both services in the background
* Map the correct ports so the app is available to users

If everything works correctly, you should now be able to access your app:

* **Frontend (Dash UI):** `http://<production-vm-ip>:8050`
* **Backend docs (FastAPI Swagger):** `http://<production-vm-ip>:8000/docs`


Certainly! Here’s a short, clean section you can copy-paste right after Step 3 — answering *“what if I want to push more changes later?”* and showing the push/pull flow between development and production:

#### 🔄 What If You Make More Changes?

If you update your code on the **development VM**, you can push new commits to GitHub like this:

```bash
git add .
git commit -m "Update something"
git push
```

Then, on the **production VM**, pull the latest changes and restart your app:

```bash
git pull
docker compose up -d --build
```

This fetches your updates, rebuilds the containers, and applies the changes — all with just two commands.

#### ✅ This Is the Power of Docker

This simple, consistent deployment process is **why containerization matters**.

You didn’t have to:

* Install any Python packages
* Set up environments
* Download datasets
* Configure servers manually

Just `docker compose up`, and your app is running — exactly the same way it did on your development VM.

#### 🔁 Step 4 – Test Automatic Service Recovery

In real-world production, servers **reboot** — due to maintenance, crashes, or hardware updates. Your services need to come back online **automatically**.

That’s what this line in `docker-compose.yml` does:

```yaml
restart: always
```

Let’s test that behavior:

```bash
sudo reboot
```

After the VM restarts (wait 1–2 minutes), visit the same URLs again:

* `http://<production-vm-ip>:8050`
* `http://<production-vm-ip>:8000/docs`

You should find that everything comes back online **without any manual intervention**.

### ⭐ Bonus Exercise

#### Push to Docker Hub or Quay (Optional)

Right now, every time you deploy on a new machine, Docker has to **rebuild your images from source**. That’s fine for small projects, but slow and unnecessary for real-world production setups.

A more efficient approach is to **build your images once**, push them to a container registry like **Docker Hub** or **Quay.io**, and then **pull** those prebuilt images on any machine.

Here’s how:

1. **Build and tag your backend image:**

```bash
docker tag grocery-backend REGISTRY/YOURNAME/grocery-backend:v1.0
docker push REGISTRY/YOURNAME/grocery-backend:v1.0
```

You have to create a Docker Hub or Quay.io account for this to work.

2. **Update `docker-compose.yml` to use the prebuilt image:**

```yaml
services:
  backend:
    image: yourname/grocery-backend:v1.0
    ports:
      - "8000:8000"
    restart: always
```

(You can still build the frontend locally, or push that one too.)

3. **On the production VM:**

```bash
docker compose pull
docker compose up -d
```

Now your backend service is pulled from Docker Hub — no need to build it again.

➡️ This is especially useful when deploying to multiple environments, using CI/CD, or handing off work to teammates.

### ✅ Summary

By the end of this lab, you:

* Used **Docker Compose** to simplify deployment and app structure
* Created a clean separation between backend and frontend services
* Deployed to a **production VM** via Git and SSH
* Enabled **automatic restarts** for long-running services
* (Optionally) pushed **prebuilt Docker images** to a registry for smoother deployment

Nice work — you’ve now containerized, versioned, and deployed a **production-ready machine learning app**!
