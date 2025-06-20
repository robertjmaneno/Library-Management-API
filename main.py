
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "isbn": "978-0743273565",
        "published_year": 1925,
        "available": True
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "978-0061120084",
        "published_year": 1960,
        "available": True
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "isbn": "978-0451524935",
        "published_year": 1949,
        "available": False
    }
]

app = FastAPI()

@app.get("/get_books")
async def get_books():
    pass

@app.get("/get_book/{book_id}")
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


