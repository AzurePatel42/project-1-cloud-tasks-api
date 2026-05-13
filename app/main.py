from fastapi import FastAPI
from .routers import tasks
from .database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Cloud Tasks API")

# Include routers
app.include_router(tasks.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Cloud Tasks API is running!"}
