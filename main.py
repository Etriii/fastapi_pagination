from sqlmodel import Session, select
from sqlalchemy import func
from fastapi import FastAPI, Depends, Query
from db import get_db, create_db_and_tables
from contextlib import asynccontextmanager
from schemas import PaginationListResponse
from models import LotsOfDataForPagination


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connecting to DB...")
    try:
        create_db_and_tables()
        print("Tables created.")
    except Exception as e:
        print(f"Failed to create DB tables: {e}")

    yield

    print("Disconnecting from DB...")


version = "v1"

app = FastAPI(
    lifespan=lifespan, title="API NP", description="An API for Secret", version=version
)


# @app.get(f"/api/{version}/paginated-data", response_model=PaginationListResponse)
# def get_paginated_data(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(5, ge=1, le=100),
#     session: Session = Depends(get_db),
# ):
#     total_entries = session.exec(
#         select(func.count()).select_from(LotsOfDataForPagination)
#     ).one()

#     total_pages = (total_entries + per_page - 1) // per_page

#     offset = (page - 1) * per_page
#     results = session.exec(
#         select(LotsOfDataForPagination).offset(offset).limit(per_page)
#     ).all()

#     return {
#         "status": "success",
#         "current_page": page,
#         "per_page": per_page,
#         "total_entries": total_entries,
#         "total_pages": total_pages,
#         "data": results,
#     }


from typing import Type, TypeVar
from sqlmodel import Session, SQLModel, select
from sqlalchemy import func

T = TypeVar("T", bound=SQLModel)  # Generic type for SQLModel tables


def paginate(session: Session, model: Type[T], page: int = 1, per_page: int = 10):
    """Reusable pagination function for SQLModel tables."""

    total_entries = session.exec(select(func.count()).select_from(model)).one()

    total_pages = (total_entries + per_page - 1) // per_page
    offset = (page - 1) * per_page

    results = session.exec(select(model).offset(offset).limit(per_page)).all()

    return {
        "status": "success",
        "current_page": page,
        "per_page": per_page,
        "total_entries": total_entries,
        "total_pages": total_pages,
        "data": results,
    }
    

@app.get(f"/api/{version}/paginated-data", response_model=PaginationListResponse)
def get_paginated_data(
    page: int = Query(1, ge=1),
    per_page: int = Query(5, ge=1, le=100),
    session: Session = Depends(get_db)
):
    return paginate(session, LotsOfDataForPagination, page, per_page)


