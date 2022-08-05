
# python3 -m uvicorn api:app --reload --port 8000
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


with open("prediction_output.json", "r") as read_file:
    data = json.load(read_file)

@app.get('/predict')
async def predict():
    return data







