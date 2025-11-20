from fastapi import FastAPI
from database.db import engine
from database import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FlowState Backend is running! 🚀"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
