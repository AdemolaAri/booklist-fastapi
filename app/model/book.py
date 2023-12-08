from pydantic import BaseModel
from pydantic import Field

class Book(BaseModel):
    title: str = Field(max_length=255)
    author: str = Field(max_length=255)
    price: float
    inventory: int = Field(default=0)

class BookInDB(Book):
    id: int