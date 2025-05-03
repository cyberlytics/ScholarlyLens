from beanie import Document
from typing import Optional, List, Dict
from pydantic import BaseModel, Field
import uuid

class Author(Document):
    name: str
    affiliation: Optional[str] = None
    interests: List[str] = []
    citations: Optional[int] = None
    h_index: Optional[int] = None
    i10_index: Optional[int] = None
    publications: List[dict] = []
    cites_per_year: Dict[str, int] = Field(default_factory=dict)

    class Settings:
        name = "authors"