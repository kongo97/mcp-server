from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modello della richiesta
class NumberRequest(BaseModel):
    value: int

# Modello della risposta
class DoubleResponse(BaseModel):
    result: int

# hello world
@app.get("/")
def read_root():
    return {"Hello": "World"}

# gmail inbox (EXAMPLE)
@app.get("/gmail/inbox/count")
def double_number():
    mail_count = 1
    return {"inbox": mail_count}

# gmail read (EXAMPLE)
@app.get("/gmail/read/id")
def double_number():
    mail_content = "Dear Client, Some text Some text Some text Some text Some text..."
    return {"content": mail_content}