from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published : Optional[bool]

@app.get('/')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    return {'data':f'{limit}blog list'}

@app.get('/about')
def about():
    return {'data':{'name':'Fasstapi'}}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id:int):
    return {'data': {'1','2'}}

@app.post('/blog_create')
def blog(blog:Blog):
    return {'data': f"blog is created as {blog.title}"}

# if __name__ == "__main__":
    # uvicorn.run(app,host="127.0.0.1", port=9000)