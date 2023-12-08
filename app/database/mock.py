from app.model.book import BookInDB

MockBooks = [
    BookInDB(id=1, title="Northanger Abbey",
             author="Jane Austen", year_of_publication=1814, review="Great"),
    BookInDB(id=2, title="Siddhartha", author="Hermann Hesse",
             year_of_publication=2000, review="Mid"),
    BookInDB(id=3, title="The Trial", author="Franz Kafka",
             year_of_publication=1999, review="Bad"),
]
