from fastapi import FastAPI
from pydantic import BaseModel
from models import classify_email

app = FastAPI()

class EmailRequest(BaseModel):
    email_body: str

@app.post("/predict")
def predict(request: EmailRequest):
    return classify_email(request.email_body)
