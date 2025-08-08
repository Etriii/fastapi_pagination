from models import LotsOfDataForPagination
from sqlmodel import SQLModel
from typing import List, Literal

class PaginationListResponse(SQLModel):
    status: Literal["success"]
    current_page: int
    per_page: int
    total_entries: int
    total_pages: int
    data: List[LotsOfDataForPagination]
