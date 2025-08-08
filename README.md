# FastAPI Pagination Example with SQLModel

This project demonstrates how to implement **pagination** in a FastAPI application using **SQLModel** (a combination of SQLAlchemy and Pydantic).

It uses a SQLite database and includes **dummy seed data** on startup.

---

## 🚀 Features

- Pagination with `page` and `per_page` query parameters
- Validated response schema
- SQLModel integration
- Automatic database creation and seeding
- SQLite database (lightweight and file-based)

---

## 📦 Requirements

Make sure you have **Python 3.9+** installed.

Install dependencies:

```bash
pip install -r requirements.txt 
```

## To run
```bash
python -m uvicorn app:main --reload
```

then try it on docs:
```bash
http://127.0.0.1:8000/docs
```


