SELECT product_name, year, price
FROM Sales
JOIN Product P
ON P.product_id = Sales.product_id;
