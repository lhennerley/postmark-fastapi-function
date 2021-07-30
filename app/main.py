import secrets

from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
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

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "test")
    correct_password = secrets.compare_digest(credentials.password, "test")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/")
def root():
    return "Running"

@app.post("/inbound")
def inbound_mail(mail: PostmarkEmail, username = Depends(get_current_username)):
    print(mail.From)
    print(mail.Subject)
    print(mail.TextBody)