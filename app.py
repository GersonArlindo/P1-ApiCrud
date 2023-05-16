from fastapi import FastAPI

app = FastAPI()

app.get('/')
def read_root():
    return{"Welcome": "wolcome to my REST API"}
