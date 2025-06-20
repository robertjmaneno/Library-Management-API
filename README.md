# Library Management API

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)
[![GitHub Issues](https://img.shields.io/github/issues/robertjmaneno/library-management-api.svg)](https://github.com/robertjmaneno/library-management-api/issues)
[![GitHub Contributors](https://img.shields.io/github/contributors/robertjmaneno/library-management-api.svg)](https://github.com/robertjmaneno/library-management-api/graphs/contributors)
[![Last Commit](https://img.shields.io/github/last-commit/robertjmaneno/library-management-api.svg)](https://github.com/robertjmaneno/library-management-api/commits/main)
[![Latest Release](https://img.shields.io/github/v/release/robertjmaneno/library-management-api.svg)](https://github.com/robertjmaneno/library-management-api/releases)

---

## Project Overview
The Library Management API is a backend web application designed to streamline and automate library operations. It manages book inventories, user reviews, and provides intelligent book recommendations using machine learning. Built with FastAPI and PostgreSQL, the API is robust, scalable, and ready for integration with any frontend or third-party system.

---

## Objectives
- **Efficient Library Operations:** Automate book management, borrowing, returning, and review collection.
- **Intelligent Recommendations:** Leverage machine learning to suggest books tailored to user preferences.
- **Role-based Access Control:** Secure sensitive operations with user roles (e.g., Admin, User).
- **Developer-Friendly:** Provide clear, interactive API documentation and easy integration points.
- **Scalable Architecture:** Use modern technologies for high performance and future growth.
- **Continuous Integration/Deployment:** Enable rapid development and deployment with best practices.

---

## Features

### User & Session Management
- User registration and authentication
- Role-based access (Admin, User)
- Secure session handling

### Library Administration
- CRUD operations for books
- Book borrowing and returning
- Book availability tracking

### Reviews & Recommendations
- Submit and manage book reviews with ratings
- Retrieve reviews for each book
- ML-based book recommendations (collaborative filtering)

### API & Documentation
- RESTful endpoints for all operations
- Interactive API docs (Swagger UI)
- Input validation with Pydantic

---

## Database Design
The API uses a PostgreSQL database with a normalized schema, including:
- **Users & Roles:** For authentication and access control
- **Books:** Book details and inventory
- **Reviews:** User-submitted ratings and comments
- **Borrow Records:** Track which user has borrowed which book and when

> For a detailed overview of the database schema, see the [Database Design Documentation](#).

---

## Architecture
- **Backend API:** FastAPI, exposing RESTful endpoints for all library operations
- **Database:** PostgreSQL for persistent data storage
- **ORM:** SQLModel for database operations
- **Machine Learning:** Scikit-learn and Pandas for recommendations
- **Containerization:** (Optional) Docker for development and deployment
- **CI/CD:** (Optional) GitHub Actions for automated testing and deployment

---

## Development Workflow
For setup and development instructions, see the [Development Documentation](#).

**Quick Start:**
1. Clone the repository:
   ```sh
   git clone https://github.com/robertjmaneno/library-management-api.git
   cd library-management-api
   ```
2. Set up a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   # On Unix/macOS
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Configure your PostgreSQL database and update the connection string in `config.py`.
4. Run database migrations:
   ```sh
   alembic upgrade head
   ```
5. Start the application:
   ```sh
   uvicorn main:app --reload
   ```
6. Access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Deployment Workflow
For deployment instructions, see the [Deployment Documentation](#).

- Use a production-grade ASGI server (e.g., Uvicorn or Hypercorn)
- Set up a reverse proxy (e.g., Nginx) for SSL and load balancing
- Configure environment variables for database and ML settings
- Example:
  ```sh
  uvicorn main:app --host 0.0.0.0 --port 8000
  ```

---

## Contributing 🤝
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Make your changes and commit:
   ```sh
   git commit -am 'Add new feature'
   ```
4. Push to the branch:
   ```sh
   git push origin feature-branch
   ```
5. Create a new Pull Request.

---

## Licensing 📄
Library Management API is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements 🙌
Special thanks to the developers of FastAPI, SQLModel, PostgreSQL, Scikit-learn, and Pydantic for their excellent tools and libraries.

---

## Tech Stack

- **FastAPI:** API framework
- **PostgreSQL:** Relational database
- **SQLModel:** ORM for database operations
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

## Contact

For questions or feedback, reach out to [robertjmaneno@gmail.com](mailto:robertjmaneno@gmail.com).

---

## Recommended Reading

- **PostgreSQL:** _PostgreSQL: Up and Running_ by Regina Obe and Leo Hsu
- **Machine Learning:** _Machine Learning for Hackers_ by Drew Conway and John Myles White


## Machine Learning Recommendations

> **Note:** The ML-based book recommendation system is currently under development and training. This feature will be available in a future release.