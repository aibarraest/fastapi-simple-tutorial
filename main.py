import random

from fastapi import FastAPI

app = FastAPI()  # Instance the FastAPI object


@app.get("/")
def index():
    return {"message": "Hello World!"}


@app.get(
    "/random",
    summary="Returns a random number",
    description="""This endpoint is used to generate a random number from 0 to 100."""
)
def get_random_number():
    return random.randint(0, 100)
