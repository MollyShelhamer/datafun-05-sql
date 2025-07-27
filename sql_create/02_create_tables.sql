CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL
);


CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT,
    year_published INTEGER,
    author_id TEXT
);