
# python3 -m uvicorn api:app --reload --port 8000
import json
# ممكن اعمل انه بالانتر كوماند اضل اشغل السكربت واعبي بالجيسون فايل و عند الapi اضل ارجعه

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


with open("prediction_output.json", "r") as read_file:
    data = json.load(read_file)

@app.post('/predict')
async def predict():
    return data







