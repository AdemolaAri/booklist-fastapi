from fastapi import FastAPI
from booklist.api.v1.endpoints import book

app = FastAPI(title='Booklist API')

# Include the router from the book endpoint
app.include_router(book.router)