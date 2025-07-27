SELECT author_id, COUNT(*) AS total_books
FROM books
GROUP BY author_id
