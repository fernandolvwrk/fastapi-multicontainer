"""
This is an example application prepared for a multi-container setup in Docker
The complete app is made up of two FastAPI web applications. The main application exposes three REST API services.
/ and /ping are simple ping services
/hidden makes a call to the secondary application, installed in another container accessible through the internal network.
"""

import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"code": 0, "data": "/ I am the entry point of the app and I am alive"}

@app.get("/ping")
async def ping():
    return {"code": 0, "data": "/ping: I am alive. Ping is working fine"}

@app.get("/hidden")
async def hidden():
    completion_url = "http://api2:8001/"
    aa = requests.get(completion_url)
    return {"code": 0, "data": f"{aa.text}"}

