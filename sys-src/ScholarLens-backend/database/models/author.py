from beanie import Document, Link
from typing import Optional, List, TYPE_CHECKING, ForwardRef
from pydantic import BaseModel, Field
import uuid

if TYPE_CHECKING:
    from .publication import Publication
    from .institut import Institut

class Author(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    google_scholar_id: str
    name: str
    institut: Link["Institut"] = Field(...)
    publications: List[Link["Publication"]] = []
    interest: List[str] = []
    email: str
    h_index: int
    i10_index: int
    citation: int
    h_index5y: int
    i10_index5y: int
    citation5y: int
    cited_by_years: List[int] = []

    class Settings:
        name = "authors"