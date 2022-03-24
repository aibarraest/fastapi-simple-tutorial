import random  # Imports Python library that generates pseudo-random numbers
from fastapi import FastAPI  # Imports FastAPI object

app = FastAPI()  # Instances the FastAPI object


@app.get("/")
def index():
    return {"message": "Hello World!"}


@app.get("/random-number")
def get_random_number():
    return random.randint(0, 100)
