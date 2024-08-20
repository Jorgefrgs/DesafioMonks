from typing import List, Dict

from pydantic import BaseModel


class PostData(BaseModel):
    github_url: str
    name: str
    pop_ranking: List[Dict[str, str]]
    genre_ranking: List[str]
