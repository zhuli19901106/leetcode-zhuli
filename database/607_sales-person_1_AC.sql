-- https://leetcode.com/problems/sales-person/ 
-- 1AC, three way join
SELECT s.name 
FROM   salesperson s 
       LEFT JOIN (SELECT c.com_id, 
                         c.name, 
                         o.sales_id 
                  FROM   company c 
                         INNER JOIN orders o 
                                 ON c.com_id = o.com_id 
                  WHERE  c.name = 'RED') co 
              ON s.sales_id = co.sales_id 
WHERE  co.sales_id IS NULL; 
