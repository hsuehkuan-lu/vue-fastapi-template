# Vue 3 + FastAPI + Docker Template

This project provides a starter template integrating a **Vue 3 (TypeScript + Vite)** frontend, a **FastAPI (Python)** backend, and **Docker** orchestration. 

It's designed to be a simple, robust foundation for your next web application.

## 🚀 Quick Start (Docker)

The easiest way to run the entire stack is using Docker Compose. This will spin up the backend API, build the frontend, and serve it via Nginx, wiring up the networks automatically.

1.  Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
2.  From the **root of the repository** (where `docker-compose.yml` is located), run:

```bash
docker-compose up -d --build
```

3.  Open your browser to `http://localhost`. You should see the Vue frontend successfully calling the backend API!

*   **Frontend**: `http://localhost`
*   **Backend API**: `http://localhost/api/hello`
*   **Backend Docs (Swagger UI)**: `http://localhost:8000/docs`

## 🛠️ Local Development (Without Docker)

If you prefer to run the services locally for development with hot-reloading:

### 1. Start the Backend (FastAPI)

Open a terminal and navigate to the `backend` directory:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
*The backend will run on `http://127.0.0.1:8000`.*

### 2. Start the Frontend (Vue 3 / Vite)

Open a **new** terminal and navigate to the `frontend` directory:

```bash
cd frontend
npm install
npm run dev
```
*Vite will start the dev server (usually on `http://localhost:5173`). Vite is configured to proxy requests starting with `/api` to the backend running on port `8000`. So, you don't have to worry about CORS during development!*

## �️ Database Migrations (Alembic)

This project uses SQLAlchemy for the ORM and Alembic for database migrations. The database is configured as a local SQLite database (`app.db`).

### Running Migrations

To apply existing migrations and create the database tables:
```bash
cd backend
alembic upgrade head
```

### Generating New Migrations

After modifying or adding new SQLAlchemy models in `backend/models.py`, generate a new migration script and apply it:
```bash
cd backend
alembic revision --autogenerate -m "Description of your changes"
alembic upgrade head
```

## 🔌 API Client Generation (OpenAPI)

Since FastAPI automatically generates an OpenAPI specification, we use `@hey-api/openapi-ts` to automatically generate strongly-typed TypeScript clients and interfaces for your Vue frontend.

### Generating the Client

1. Ensure your backend is running locally (`cd backend && uvicorn main:app --reload --host 127.0.0.1 --port 8000`).
2. Open a terminal in the `frontend` directory and run:

```bash
cd frontend
npm run generate-api
```

This will fetch the `openapi.json` from the backend and populate the `frontend/src/api/` folder with exported services and models you can import directly into your `.vue` components.

## �📁 Project Structure

*   **/frontend**: Vue 3 application initialized with Vite.
    *   `src/App.vue`: Contains the example API fetch logic.
    *   `vite.config.ts`: Configured with an `/api` proxy for local dev.
    *   `Dockerfile` & `nginx.conf`: Multi-stage Docker build, serving static files over Nginx and reverse-proxying `/api` requests to the `backend` container.
*   **/backend**: FastAPI application.
    *   `main.py`: Contains basic API routes (`/api/hello`) and CORS configuration.
    *   `requirements.txt`: Python dependencies.
    *   `Dockerfile`: Simple Python runner for uvicorn.
*   `docker-compose.yml`: Ties the frontend and backend containers together into a unified local network.
