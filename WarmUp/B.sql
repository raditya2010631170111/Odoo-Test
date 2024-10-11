SELECT books.title AS book_title, authors.name AS author_name 
FROM books
JOIN authors ON books.author_id = authors.book_id
WHERE books.price > 20;

SELECT a.name AS author_name, COUNT(b.id) as book_count
FROM authors a
LEFT JOIN books b ON a.id = b.author_id AND b.publish_year >= 2000
GROUP BY a.name
HAVING COUNT(b.id) > 3;

WITH book_totals AS (
  SELECT author_id, SUM(price) as total_price
  FROM books
  GROUP BY author_id
)
SELECT a.name, AS author_name, bt.total_price
FROM authors a
JOIN book_totals bt ON a.id = bt.author_id
WHERE bt.total_price > 1000
ORDER BY a.name;