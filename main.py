from fastapi import FastAPI, UploadFile, File
import pandas as pd
from optimizer import DeliveryOptimizer

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Delivery Optimization API is running!"}
