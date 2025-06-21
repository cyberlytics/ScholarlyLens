# database/models/institut.py
from beanie import BackLink, Document
from typing import Optional, List
from pydantic import Field
import uuid

from database.models.author import Author

class Institut(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    domain: List[str] = []
    webpage: List[str] = []
    country: str
    country_code: str
    province: Optional[str] = None
    authors: List[BackLink["Author"]] = Field(original_field="institut", default=[])

    class Settings:
        name = "institutes"
