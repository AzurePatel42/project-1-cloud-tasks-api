# Project 1 — Cloud Tasks API  
<p align="left">

  <!-- Python -->
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />

  <!-- FastAPI -->
  <img src="https://img.shields.io/badge/FastAPI-Tasks%20API-009688?style=for-the-badge&logo=fastapi&logoColor=white" />

  <!-- SQLite -->
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />

  <!-- Docker -->
  <img src="https://img.shields.io/badge/Docker-Containerized-0db7ed?style=for-the-badge&logo=docker&logoColor=white" />

  <!-- Azure Container Apps -->
  <img src="https://img.shields.io/badge/Azure-Container%20Apps-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" />

  <!-- GitHub Actions -->
  <img src="https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />

</p>
<img src="https://img.shields.io/badge/Deployed%20on-Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" />


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

## API Endpoints
✈️ API Endpoints (Pilot / Airport / Airplane Analogy)
Your API works like an airport passenger management system.
Each task = a passenger.
Your FastAPI backend = air‑traffic control.
You (the developer) = the pilot.

Below are the endpoints and what they mean in the analogy.

Create a Task
POST /tasks/  
🛫 Add a new passenger to the airplane.

Request

json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}
Response

json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}
Get All Tasks
GET /tasks/  
🧾 View the full passenger list before takeoff.

Response

json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false
  },
  {
    "id": 2,
    "title": "Finish project",
    "description": "Complete FastAPI backend",
    "completed": true
  }
]
Get a Single Task
GET /tasks/1  
🎫 Check one passenger’s ticket.

Response

json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}
Update a Task
PUT /tasks/1  
🛠️ Update a passenger’s seat or details.

Request

json
{
  "title": "Buy groceries and fruits",
  "description": "Milk, eggs, bread, apples",
  "completed": false
}
Response

json
{
  "id": 1,
  "title": "Buy groceries and fruits",
  "description": "Milk, eggs, bread, apples",
  "completed": false
}
Delete a Task
DELETE /tasks/1  
❌ Remove a passenger from the flight.

Response

json
{
  "message": "Task deleted successfully"
}
