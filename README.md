# Project 1 — Cloud Tasks API  
FastAPI backend with SQLite, Docker, and Azure deployment.

## 🚀 Features
- FastAPI CRUD API for managing tasks  
- SQLite database (local development)  
- Dockerfile for containerization  
- docker-compose for local orchestration  
- Ready for Azure Container Apps deployment  
- Clean project structure

## 📁 Project Structure
project-1-cloud-tasks-api/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── routers/
│       └── tasks.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

## ▶️ Running Locally

### 1. Install dependencies
pip install -r requirements.txt

### 2. Start the API
uvicorn app.main:app --reload

### 3. Open Swagger UI
http://localhost:8000/docs

## 🐳 Running with Docker

docker build -t tasks-api .
docker run -p 8000:8000 tasks-api

## ☁️ Deploying to Azure (Container Apps)

az login
az group create --name tasks-api-rg --location eastus
az containerapp up --name tasks-api --resource-group tasks-api-rg --image <your-image>
