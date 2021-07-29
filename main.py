from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class PostmarkEmail(BaseModel):
    From: str
    MessageStream: str
    FromName: str
    To: str
    Subject: str
    TextBody: str
    HtmlBody: str

app = FastAPI()

@app.get("/")
def root():
    return "Running"

@app.post("/inbound")
def inbound_mail(mail: PostmarkEmail):
    print(mail.From)