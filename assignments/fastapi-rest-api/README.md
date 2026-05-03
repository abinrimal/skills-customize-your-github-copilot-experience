# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will build a small RESTful API using the FastAPI framework. The assignment focuses on defining routes, request/response models, input validation, and using the built-in interactive documentation. By the end, students will have a working API they can run locally and test with curl or the Swagger UI.

## 📝 Tasks

### 🛠️ Create a Basic CRUD API

#### Description
Implement a small API that manages an in-memory collection of items (for example, products or notes). Provide endpoints to create, read, update, and delete items. Use Pydantic models for request validation and responses.

#### Requirements
Completed project should:

- Use FastAPI to define an application and expose routes.
- Define Pydantic models for request bodies and responses.
- Implement these endpoints at minimum:
  - `GET /items` — list all items
  - `GET /items/{item_id}` — retrieve a single item by id
  - `POST /items` — create a new item
  - `PUT /items/{item_id}` — update an existing item
  - `DELETE /items/{item_id}` — delete an item
- Validate input and return appropriate HTTP status codes (e.g., 201 for created, 404 for not found).
- Keep storage in-memory (a Python dict) so the app runs without external services.
- Provide clear examples of request/response bodies in the README or code comments.

Example request/response (JSON):

```
POST /items
{
  "name": "Notebook",
  "price": 9.99,
  "in_stock": true
}

201 Created
{
  "id": 1,
  "name": "Notebook",
  "price": 9.99,
  "in_stock": true
}
```

### 🛠️ Optional Enhancements

#### Description
Add one or more of the following to deepen understanding and add polish.

#### Requirements

- Add query parameters to filter or sort results (e.g., `?in_stock=true`).
- Add request/response examples in the Pydantic models so Swagger shows them.
- Persist data to a simple JSON file between restarts.
- Add authentication (simple API key) for write operations.

---

Starter files:

- `starter-app.py` — minimal FastAPI application to run and extend
- `requirements.txt` — dependencies to install (FastAPI, uvicorn)

Running locally (example):

```bash
python -m pip install -r requirements.txt
uvicorn starter-app:app --reload
```

Visit the interactive docs at `http://127.0.0.1:8000/docs`.
