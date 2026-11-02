from app.database.database import engine, Base
from app.database import models

from fastapi import FastAPI
from app.routes.jobs import router as jobs_router

app = FastAPI(title="ApplyFlow API")
Base.metadata.create_all(bind=engine)

app.include_router(jobs_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to ApplyFlow!",
        "status": "Backend is running"
    }


@app.get("/about")
def about():
    return {
        "project": "ApplyFlow",
        "purpose": "Smart Job Application Platform",
        "version": "1.0"
    }
