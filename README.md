Library Management API
This is a Library Management API built with FastAPI, designed to manage a library's book inventory, user reviews, and provide book recommendations using machine learning. The API uses PostgreSQL as the database for robust and scalable data management. It supports CRUD operations for books, user reviews, and integrates a machine learning-based recommendation system using collaborative filtering.
Features

CRUD Operations for Books: Create, read, update, and delete books.
Book Reviews: Allow users to submit, retrieve, and manage book reviews with ratings.
Book Recommendations: ML-based recommendations using collaborative filtering (SVD algorithm).
PostgreSQL Database: Uses PostgreSQL for reliable and scalable data storage.
FastAPI Benefits: Automatic OpenAPI documentation (Swagger UI) and high performance.
Input Validation: Uses Pydantic for data validation and serialization.
Asynchronous Support: Leverages FastAPI's async capabilities.

Tech Stack

FastAPI: API framework.
PostgreSQL: Relational database for storing books, reviews, and user data.
SQLAlchemy: ORM for database operations.
Pydantic: Data validation and serialization.
Uvicorn: ASGI server for running the API.
Scikit-learn & Pandas: For ML-based book recommendations.
Psycopg2: PostgreSQL adapter for Python.

Prerequisites

Python 3.7 or higher
PostgreSQL 15 or higher
pip (Python package manager)
Virtual environment (recommended)

Installation

Clone the Repository:
git clone https://github.com/your-username/library-management-api.git
cd library-management-api


Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt

Example requirements.txt:
fastapi==0.115.0
uvicorn==0.30.6
sqlalchemy==2.0.35
pydantic==2.9.2
psycopg2-binary==2.9.9
scikit-learn==1.5.1
pandas==2.2.2
numpy==1.26.4


Set Up PostgreSQL:

Install PostgreSQL and create a database named library_db.
Update the database connection string in the configuration file (e.g., config.py):DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/library_db"


Run database migrations Alembic:alembic upgrade head




Set Up ML Model:

The recommendation system uses Singular Value Decomposition (SVD) from scikit-learn for collaborative filtering.
Preprocess the review data to generate a user-item rating matrix and train the SVD model (handled automatically on startup if review data exists).
Example datasets can be sourced from open data (e.g., Book-Crossing dataset) or populated via the review endpoints.


Run the Application:
uvicorn main:app --reload


The API will be available at http://127.0.0.1:8000.
The --reload flag enables auto-reload for development.



API Endpoints
The API provides the following endpoints (see full documentation at /docs):



Method
Endpoint
Description



GET
/books
Retrieve a list of all books


GET
/books/{book_id}
Retrieve details of a specific book


POST
/books
Add a new book


PUT
/books/{book_id}
Update an existing book


DELETE
/books/{book_id}
Delete a book


POST
/books/{book_id}/borrow
Mark a book as borrowed


POST
/books/{book_id}/return
Mark a book as returned


POST
/books/{book_id}/reviews
Submit a review and rating for a book


GET
/books/{book_id}/reviews
Retrieve all reviews for a book


GET
/recommendations/{user_id}
Get book recommendations for a user (ML-based)


Example Requests
Add a New Book:
curl -X POST "http://127.0.0.1:8000/books" -H "Content-Type: application/json" -d '{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "978-0743273565",
  "published_year": 1925,
  "available": true
}'

Response:
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "978-0743273565",
  "published_year": 1925,
  "available": true
}

Submit a Review:
curl -X POST "http://127.0.0.1:8000/books/1/reviews" -H "Content-Type: application/json" -d '{
  "user_id": 1,
  "rating": 5,
  "review_text": "A timeless classic!"
}'

Response:
{
  "id": 1,
  "book_id": 1,
  "user_id": 1,
  "rating": 5,
  "review_text": "A timeless classic!",
  "created_at": "2025-06-17T13:48:00"
}

Get Recommendations:
curl -X GET "http://127.0.0.1:8000/recommendations/1"

Response:
[
  {
    "id": 2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "isbn": "978-0446310789",
    "published_year": 1960,
    "available": true
  },
  ...
]

Database Schema
Books:

id: Integer, Primary Key
title: String, Required
author: String, Required
isbn: String, Unique
published_year: Integer, Optional
available: Boolean, Default True

Reviews:

id: Integer, Primary Key
book_id: Integer, Foreign Key (Books)
user_id: Integer, Foreign Key (Users)
rating: Integer (1-5), Required
review_text: Text, Optional
created_at: Timestamp, Default Now

Users (for reviews and recommendations):

id: Integer, Primary Key
username: String, Unique
email: String, Optional

ML-Based Recommendation System

Algorithm: Uses Singular Value Decomposition (SVD) from scikit-learn for collaborative filtering.
Data: Builds a user-item matrix from review ratings.
Process:
Extract ratings from the Reviews table.
Create a sparse user-item matrix using Pandas.
Train the SVD model to predict ratings for unrated books.
Recommend top-N books with the highest predicted ratings for a given user.


Dependencies: Requires scikit-learn, pandas, and numpy.
Note: The system improves with more review data. Initial recommendations may be limited if the dataset is small.

Documentation

Interactive API documentation (Swagger UI): http://127.0.0.1:8000/docs.
Raw OpenAPI schema: http://127.0.0.1:8000/openapi.json.

Running Tests
To run tests (if included), use pytest:
pip install pytest
pytest

Deployment
To deploy the API to production:

Use a production-grade ASGI server (e.g., Uvicorn or Hypercorn).
Set up a reverse proxy (e.g., Nginx) for load balancing and SSL.
Configure environment variables for database connections and ML model settings.
Example deployment with Uvicorn:uvicorn main:app --host 0.0.0.0 --port 8000



Contributing

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make changes and commit (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Open a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or feedback, reach out to your-email@example.com.
Recommended Reading
For those interested in learning more about PostgreSQL and machine learning for recommendation systems, consider:

PostgreSQL: "PostgreSQL: Up and Running" by Regina Obe and Leo Hsu – A practical guide to PostgreSQL features and administration.
Machine Learning: "Machine Learning for Hackers" by Drew Conway and John Myles White – Covers practical ML applications, including recommendation systems, using R (adaptable to Python).
Recommendation Systems: Explore the Book-Crossing dataset on Kaggle for additional data to enhance the recommendation system.

