from sqlalchemy import Column, String
from datetime import datetime
from sqlmodel import SQLModel, Field


class LotsOfDataForPagination(SQLModel, table=True):
    __tablename__ = "lotsofdataforpagination"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(100)))
    created_at: datetime = Field(default_factory=datetime.now)