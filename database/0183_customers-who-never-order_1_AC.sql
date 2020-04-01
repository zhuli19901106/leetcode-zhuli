-- https://leetcode.com/problems/customers-who-never-order/ 
-- 1AC
SELECT c.name Customers 
FROM   customers c 
       LEFT JOIN orders o 
              ON c.id = o.customerid 
WHERE  o.customerid IS NULL; 
