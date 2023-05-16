from fastapi import FastAPI

app = FastAPI()

posts = []

@app.get('/')
def read_root():
    return{"Welcome": "wolcome to my REST API"}

@app.get('/posts')
def get_posts():
    return posts
