
## Lab 07 – Compose Deployment

<img src="../../media/docker-compose-octopus.jpg" style="width: 300px" align="right">

> Use Docker Compose to launch your entire application stack (API + frontend) with a single command.

### 🎯 Goal

Run your full machine learning application, using a **single command**:

```bash
docker compose up
```

By the end of this section, both your backend (model API) and frontend (user interface) will be running in containers — networked together automatically, with no manual container juggling.

### 🗂️ What’s Already Provided?

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

### ▶️ Build and Run the Application

From the `07-compose-deployment` folder, run:

```bash
docker compose up -d --build
```

This command:

* Builds Docker images for the backend and frontend
* Starts both containers in the background (`-d` = detached mode)
* We force rebuild images, useful when we changed the Dockerfile or code (`--build`)
* Automatically connects them to the same internal network
* Maps the correct ports to your VM so you can access them in a browser (defined in `docker-compose.yml`)

> 🧠 Tip: The `docker-compose.yml` becomes your **one-stop definition** for running the entire system. No more remembering long `docker run` commands!

### 🌐 Test the Application

Once the containers are running:

1. Open your browser and visit:
   `http://<your-vm-ip>:8050`
   → You should see the Dash interface.

2. Click **"Predict random image"**
   → It should load an image and display a prediction — meaning the frontend and backend are talking to each other.

3. To access the FastAPI docs, go to:
   `http://<your-vm-ip>:8000/docs`
   → This is the Swagger UI automatically provided by FastAPI.

### 🔍 Useful Docker Compose Commands

Here are some handy commands for managing your project with Compose:

```bash
docker compose up --build   # Rebuild images and start services
docker compose down         # Stop and remove all containers
docker compose logs         # Show logs from both containers
docker compose restart      # Restart all services
docker ps                   # Show currently running containers
```

> 🔁 If you make code changes, use `docker compose up --build` to rebuild the images.

### 🔁 Test Automatic Service Recovery

In real-world production, servers **reboot** — due to maintenance, crashes, or hardware updates. Your services need to come back online **automatically**.

That’s what this line in `docker-compose.yml` does:

```yaml
restart: always
```

Let’s test that behavior:

```bash
sudo reboot
```

After the VM restarts (wait a few seconds), visit the same URLs again:

* `http://<your-vm-ip>:8050`
* `http://<your-vm-ip>:8000/docs`

You should find that everything comes back online **without any manual intervention**.
