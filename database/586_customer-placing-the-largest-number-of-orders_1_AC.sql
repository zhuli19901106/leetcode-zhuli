-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/ 
-- 1AC
SELECT customer_number 
FROM   orders 
GROUP  BY customer_number 
HAVING Count(order_number) = (SELECT Count(order_number) con 
                              FROM   orders 
                              GROUP  BY customer_number 
                              ORDER  BY con DESC 
                              LIMIT  1); 
