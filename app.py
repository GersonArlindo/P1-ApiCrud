from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uid

app = FastAPI()

posts = []

#Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

@app.get('/')
def read_root():
    return{"Welcome": "wolcome to my REST API"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post: Post):
    post.id = str(uid())
    posts.append(post.dict())
    return posts[-1] #Obteniendo el ultimo objeto agregado

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post Not Found")
