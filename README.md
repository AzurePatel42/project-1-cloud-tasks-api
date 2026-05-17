# **Project 1 — Cloud Tasks API**

<p align="left">

  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-Tasks%20API-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Containerized-0db7ed?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Azure-Container%20Apps-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/Deployed%20on-Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" />

</p>

A lightweight, cloud‑ready **Task Management API** built with FastAPI and SQLite, containerized with Docker, and deployable to Azure Container Apps.

---

## 📌 **Overview**

This API provides a simple, production‑ready backend for managing tasks using:

- FastAPI (Python)
- SQLite database
- Docker containerization
- Azure Container Apps deployment
- Automatic Swagger documentation

✔ Supports full CRUD operations  
✔ Clean project structure  
✔ Cloud‑ready architecture  

---

## 🏗️ **Architecture**

```
                ┌──────────────────────────┐
                │      FastAPI Backend     │
                │  (app/main.py, routers)  │
                └─────────────┬────────────┘
                              │
                              │ SQLite (tasks.db)
                              ▼
                ┌──────────────────────────┐
                │        SQLite DB         │
                │   (local file storage)   │
                └──────────────────────────┘

                ┌──────────────────────────┐
                │      Docker Container    │
                │  (FastAPI + SQLite)      │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │  Azure Container Apps    │
                │   (public HTTPS API)     │
                └──────────────────────────┘
```

---

## 📁 **Project Structure**

```
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
```

---

## ▶️ **Running Locally**

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Start the API

```
uvicorn app.main:app --reload
```

### 3️⃣ Open Swagger UI

```
http://localhost:8000/docs
```

---

## 🐳 **Running with Docker**

### Build the image

```
docker build -t tasks-api .
```

### Run the container

```
docker run -p 8000:8000 tasks-api
```

---

## ☁️ **Deploying to Azure (Container Apps)**

### Login

```
az login
```

### Create Resource Group

```
az group create --name tasks-api-rg --location eastus
```

### Build & Push Image to ACR  
(Replace `<ACR_NAME>`)

```
az acr build --registry <ACR_NAME> --image tasks-api:v1 .
```

### Deploy to Azure Container Apps

```
az containerapp up \
  --name tasks-api \
  --resource-group tasks-api-rg \
  --image <ACR_NAME>.azurecr.io/tasks-api:v1 \
  --target-port 8000 \
  --ingress external
```

---

# ✈️ **API Endpoints (Airport Analogy)**  
Your API works like an **airport passenger management system**.

- Each **task = passenger**  
- FastAPI backend = **air‑traffic control**  
- You (developer) = **pilot**  

### **Create a Task**  
🛫 Add a new passenger  
`POST /tasks/`

### **Get All Tasks**  
🧾 View the passenger list  
`GET /tasks/`

### **Get a Single Task**  
🎫 Check a passenger’s ticket  
`GET /tasks/{id}`

### **Update a Task**  
🛠️ Update passenger details  
`PUT /tasks/{id}`

### **Delete a Task**  
❌ Remove a passenger  
`DELETE /tasks/{id}`

---

## 📝 **About**

Cloud Tasks API using FastAPI, SQLite, Docker, and Azure Container Apps.
