-- https://leetcode.com/problems/customers-who-bought-all-products/
-- 1AC
SELECT customer_id 
FROM   customer 
GROUP  BY customer_id 
HAVING Count(DISTINCT product_key) = (SELECT Count(DISTINCT product_key) 
                                      FROM   product); 
