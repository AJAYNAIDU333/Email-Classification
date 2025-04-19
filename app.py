from fastapi import FastAPI
from models import classify_email

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the email classification API!"}

@app.post("/classify/")
def classify(email_body: str):
    result = classify_email(email_body)
    return result
