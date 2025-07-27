SELECT books.title, authors.author_id
FROM books
JOIN authors ON books.author_id = authors.author_id