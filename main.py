"""This is the router file."""

from fastapi import FastAPI
# from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: Optional[int] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "welcome to api intergration"}

@app.post("/createposts")
async def create_post(payload: Post):
    print(payload)
    return {"data":"post created successfully.."}