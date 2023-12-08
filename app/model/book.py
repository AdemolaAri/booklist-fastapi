from pydantic import BaseModel
from pydantic import Field


class Book(BaseModel):
    title: str = Field(max_length=255)
    author: str = Field(max_length=255)
    year_of_publication: int
    review: str | None = Field(max_length=255, default=None)


class BookInDB(Book):
    id: int
