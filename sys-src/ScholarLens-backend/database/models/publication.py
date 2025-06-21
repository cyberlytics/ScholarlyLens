from beanie import Document, Link
from typing import Optional, List, Dict, TYPE_CHECKING
from pydantic import BaseModel, Field
import uuid
from datetime import date

if TYPE_CHECKING:
    from .author import Author

class Publication(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    author: Link["Author"]
    content: str
    year: Optional[int]
    citation: Optional[str]
    gs_id: Optional[str]
    citation_count: Optional[int]
    cited_by_url: Optional[str]
    cites_id: List[str] = []

    class Settings:
        name = "publications"
