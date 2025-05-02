1.
SELECT DISTINCT product_name
FROM Products;

2.
SELECT p.product_id, p.product_name, p.price
FROM Products p
JOIN Nutritional_Information n ON p.product_id = n.product_id
WHERE n.fiber > 5;

3.
SELECT p.product_name
FROM Products p
JOIN Nutritional_Information n ON p.product_id = n.product_id
ORDER BY n.protein DESC
LIMIT 1;

4.
SELECT p.category_id, SUM(p.calories) AS total_calories
FROM Products p
JOIN Nutritional_Information n ON p.product_id = n.product_id
WHERE n.fat > 0
GROUP BY p.category_id;

5.
SELECT c.category_name, ROUND(AVG(p.price), 2) AS average_price
FROM Products p
JOIN Categories c ON p.category_id = c.category_id
GROUP BY c.category_name;