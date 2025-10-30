from fastapi import FastAPI
from pydantic import BaseModel
import pickle

with open("pipeline_v1.bin", "rb") as f:
    model = pickle.load(f)


class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float


app = FastAPI()


@app.post("/predict")
def predict(lead: Lead):
    record = lead.model_dump()
    X = [record]
    prob = model.predict_proba(X)[0, 1]
    return {"subscription_probability": round(float(prob), 3)}


@app.get("/ping")
def ping():
    return {"status": "ok"}


@app.get("/")
def home():
    return {"message": "Model API is running!"}
