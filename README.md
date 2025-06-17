# Library Management API

A Library Management API built with FastAPI to manage a library's book inventory, user reviews, and provide book recommendations using machine learning. The API uses PostgreSQL for robust and scalable data management. It supports CRUD operations for books, user reviews, and integrates a machine learning-based recommendation system using collaborative filtering.

---

## Features

- **CRUD Operations for Books:** Create, read, update, and delete books.
- **Book Reviews:** Users can submit, retrieve, and manage book reviews with ratings.
- **Book Recommendations:** ML-based recommendations using collaborative filtering (SVD algorithm).
- **PostgreSQL Database:** Reliable and scalable data storage.
- **FastAPI Benefits:** Automatic OpenAPI documentation (Swagger UI) and high performance.
- **Input Validation:** Uses Pydantic for data validation and serialization.
- **Asynchronous Support:** Leverages FastAPI's async capabilities.

---

## Tech Stack

- **FastAPI:** API framework
- **PostgreSQL:** Relational database
- **SQLAlchemy:** ORM for database operations
- **Pydantic:** Data validation and serialization
- **Uvicorn:** ASGI server
- **Scikit-learn & Pandas:** ML-based recommendations
- **Psycopg2:** PostgreSQL adapter for Python

---

## Prerequisites

- Python 3.7 or higher
- PostgreSQL 15 or higher
- pip (Python package manager)
- Virtual environment (recommended)

---

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/robertjmaneno/library-management-api.git
   cd library-management-api
   ```

2. **Set Up a Virtual Environment:**
   ```sh
   python -m venv venv
   # On Unix/macOS
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   Example `requirements.txt`:
   ```
   fastapi==0.115.0
   uvicorn==0.30.6
   sqlalchemy==2.0.35
   pydantic==2.9.2
   psycopg2-binary==2.9.9
   scikit-learn==1.5.1
   pandas==2.2.2
   numpy==1.26.4
   ```

4. **Set Up PostgreSQL:**
   - Install PostgreSQL and create a database named `library_db`.
   - Update the database connection string in your configuration file (e.g., `config.py`):

     ```python
     DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/library_db"
     ```

   - Run database migrations (if using Alembic):

     ```sh
     alembic upgrade head
     ```

5. **Set Up ML Model (In Progress):**
   - The recommendation system uses SVD from scikit-learn for collaborative filtering.
   - Preprocess review data to generate a user-item rating matrix and train the SVD model (handled automatically on startup if review data exists).

---

## Running the Application

```sh
uvicorn main:app --reload
```

- The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).
- The `--reload` flag enables auto-reload for development.

---

## API Endpoints

| Method | Endpoint                      | Description                              |
|--------|-------------------------------|------------------------------------------|
| GET    | `/books`                      | Retrieve a list of all books             |
| GET    | `/books/{book_id}`            | Retrieve details of a specific book      |
| POST   | `/books`                      | Add a new book                           |
| PUT    | `/books/{book_id}`            | Update an existing book                  |
| DELETE | `/books/{book_id}`            | Delete a book                            |
| POST   | `/books/{book_id}/borrow`     | Mark a book as borrowed                  |
| POST   | `/books/{book_id}/return`     | Mark a book as returned                  |
| POST   | `/books/{book_id}/reviews`    | Submit a review and rating for a book    |
| GET    | `/books/{book_id}/reviews`    | Retrieve all reviews for a book          |
| GET    | `/recommendations/{user_id}`  | Get book recommendations for a user      |

---

## Example Requests

**Add a New Book:**
```sh
curl -X POST "http://127.0.0.1:8000/books" -H "Content-Type: application/json" -d '{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "978-0743273565",
  "published_year": 1925,
  "available": true
}'
```

**Submit a Review:**
```sh
curl -X POST "http://127.0.0.1:8000/books/1/reviews" -H "Content-Type: application/json" -d '{
  "user_id": 1,
  "rating": 5,
  "review_text": "A timeless classic!"
}'
```

**Get Recommendations:**
```sh
curl -X GET "http://127.0.0.1:8000/recommendations/1"
```

---

## Database Schema

**Books**
- `id`: Integer, Primary Key
- `title`: String, Required
- `author`: String, Required
- `isbn`: String, Unique
- `published_year`: Integer, Optional
- `available`: Boolean, Default True

**Reviews**
- `id`: Integer, Primary Key
- `book_id`: Integer, Foreign Key (Books)
- `user_id`: Integer, Foreign Key (Users)
- `rating`: Integer (1-5), Required
- `review_text`: Text, Optional
- `created_at`: Timestamp, Default Now

**Users**
- `id`: Integer, Primary Key
- `username`: String, Unique
- `email`: String, Optional

---

## ML-Based Recommendation System

- **Algorithm:** SVD from scikit-learn for collaborative filtering.
- **Data:** Builds a user-item matrix from review ratings.
- **Process:**
  1. Extract ratings from the Reviews table.
  2. Create a sparse user-item matrix using Pandas.
  3. Train the SVD model to predict ratings for unrated books.
  4. Recommend top-N books with the highest predicted ratings for a given user.

> **Note:** The system improves with more review data. Initial recommendations may be limited if the dataset is small.

---

## Documentation

- Interactive API documentation (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Raw OpenAPI schema: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## Running Tests

To run tests, use [pytest](https://docs.pytest.org/):

```sh
pip install pytest
pytest
```

---

## Deployment

- Use a production-grade ASGI server (e.g., Uvicorn or Hypercorn).
- Set up a reverse proxy (e.g., Nginx) for load balancing and SSL.
- Configure environment variables for database connections and ML model settings.

Example deployment:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Make changes and commit:
   ```sh
   git commit -m "Add feature"
   ```
4. Push to the branch:
   ```sh
   git push origin feature-branch
   ```
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For questions or feedback, reach out to [robertjmaneno@gmail.com](mailto:robertjmaneno@gmail.com).

---

## Recommended Reading

- **PostgreSQL:** _PostgreSQL: Up and Running_ by Regina Obe and Leo Hsu
- **Machine Learning:** _Machine Learning for Hackers_ by Drew Conway and John Myles White


## Machine Learning Recommendations

> **Note:** The ML-based book recommendation system is currently under development and training. This feature will be available in a future release.