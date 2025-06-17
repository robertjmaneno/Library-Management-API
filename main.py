from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def print_hello():
    return {"greeting": "Good Afternoon Robert!"}


@app.get("/greet/{name}")
async def greet(name: Optional[str] = "Robert Maneno", age:int = 23) -> dict:
    return {"greeting": f"Good Afternoon {name}! You are {age} years old."}


class CreateBook(BaseModel):
    title: str
    year: int


@app.post("/create_book")
async def create_book(create_book: CreateBook) -> dict:
    return {
        "message": "Book created successfully",
        "book": {
            "title": create_book.title,
            "year": create_book.year
        }
    }
