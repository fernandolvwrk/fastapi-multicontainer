"""
This is the secondary app. It contains thow simple ping FastAPI API REST services
"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return "I am a hidden service. I am alive. No time to make this answer pretty (sorry)"


@app.get("/secondaryping")
async def ping():
    return "I am another hidden service living on the hidding container. I am alive."

