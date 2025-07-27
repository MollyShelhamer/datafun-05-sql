CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL
);


CREATE TABLE books (
    book_id TEXT Primary Key,
    title TEXT NOT NULL,
    genre TEXT,
    year_published INTEGER,
    author_id TEXT
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);