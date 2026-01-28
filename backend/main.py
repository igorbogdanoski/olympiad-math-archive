import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_database

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "TeacherOS API is Running!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
