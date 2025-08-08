from typing import List, Literal
from sqlmodel import SQLModel, Field, Session, select
from datetime import datetime
from fastapi import FastAPI, Depends, Query
from sqlalchemy import Column, String, create_engine
from db import get_db

# === SQLModel Table ===
class LotsOfDataForPagination(SQLModel, table=True):
    __tablename__ = "lots_of_data_for_pagination"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(100)))
    created_at: datetime = Field(default_factory=datetime.now)


# === Response Schema ===
class PaginationResponse(SQLModel):
    status: Literal["success"]
    current_page: int
    per_page: int
    total_entries: int
    total_pages: int
    data: List[LotsOfDataForPagination]


# === FastAPI App ===
app = FastAPI()



# === API: Paginated Data ===
@app.get("/paginated-data", response_model=PaginationResponse)
def get_paginated_data(
    page: int = Query(1, ge=1),
    per_page: int = Query(5, ge=1, le=100),
    session: Session = Depends(get_db)
):
    total_entries = session.exec(select(LotsOfDataForPagination)).count()
    total_pages = (total_entries + per_page - 1) // per_page

    offset = (page - 1) * per_page
    results = session.exec(
        select(LotsOfDataForPagination).offset(offset).limit(per_page)
    ).all()

    return {
        "status": "success",
        "current_page": page,
        "per_page": per_page,
        "total_entries": total_entries,
        "total_pages": total_pages,
        "data": results
    }
