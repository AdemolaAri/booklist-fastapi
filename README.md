# Book Management API

This project is a simple Book Management API built with Python and FastAPI.

## Endpoints

- `GET /books`: This endpoint is used to get a list of all books in the database.

- `GET /books/{id}`: This endpoint is used to get a single book by its ID.

- `POST /books`: This endpoint is used to create a new book. It accepts a JSON body with the book details and returns a list of all books in the database, including the newly created one.

## Usage

To create a new book, send a POST request to `/books` with the following JSON body:

```json
{
  "title": "Book Title",
  "author": "Author Name",
  "year_of_publication": "Year of Publication",
  "review": "Book Review"
}
```

## Development

To run the project locally, you will need Python and FastAPI installed. Then, you can run the server with the following command:

```bash
uvicorn main:app --reload
```

This will start the server on http://localhost:8000.

## Testing

To run the tests, you will need to install pytest. Then, you can run the tests with the following command:

```bash
pytest
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have a suggestion.

## License

This project is licensed under the MIT License.
