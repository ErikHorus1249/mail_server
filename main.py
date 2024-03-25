from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from utils import export_csv

app = FastAPI()

class Info(BaseModel):
    hostname: str
    ntp: str
    
app = FastAPI()

@app.post("/checker/")
async def create_item(item: Info):
    status = export_csv(item.hostname, item.ntp)
    return True if status else False