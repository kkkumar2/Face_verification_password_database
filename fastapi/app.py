from fastapi import FastAPI ,Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.responses import HTMLResponse,FileResponse,JSONResponse
from typing import Optional,List,Union,Dict
import os
import logging
import time
from pydantic import BaseModel

app  = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST","GET"], 
    allow_headers=["*"],
    max_age=2 # how mcuh hit api per second
    )

class ClientImageInput(BaseModel):
    key: str
    username: str
    password:str


@app.get("/save_data_db")
def save_data_db(data:ClientImageInput):
    since = time.time()
    print("Predict API hitted")
    print("data is",data.username)


if __name__ == "__main__":
    uvicorn.run(app,port=8080)