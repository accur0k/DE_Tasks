DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS books_summary;

SELECT * FROM books;

CREATE TABLE books_summary AS
SELECT
    bk.year AS publication_year,
    COUNT(*) AS book_count,
    ROUND(AVG(
        CASE
            WHEN bk.price LIKE '$%' THEN SUBSTRING(bk.price FROM 2)::numeric
            WHEN bk.price LIKE '€%' THEN SUBSTRING(bk.price FROM 2)::numeric * 1.2
        END
    )::numeric, 2) AS average_price_usd
FROM books bk
GROUP BY year
ORDER BY year ASC;

SELECT * FROM books;

SELECT * FROM books_summary;