from pydantic import BaseModel
from typing import List

class RelatedPage(BaseModel):
    title: str
    url: str
    excerpt: str

class SearchRequest(BaseModel):
    query: str

class SearchResponse(BaseModel):
    summary: str
    related_pages: List[RelatedPage]
    files: List[str]