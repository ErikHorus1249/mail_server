from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from send import send_email

app = FastAPI()

class Info(BaseModel):
    hostname: str
    ntp: str
    
app = FastAPI()

@app.post("/checker/")
async def create_item(item: Info):
    sent_status = send_email(item.hostname, item.ntp)
    return True if sent_status else False