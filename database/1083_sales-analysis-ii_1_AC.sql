-- https://leetcode.com/problems/sales-analysis-ii/ 
-- 1AC, filter by percentage
SELECT sp.buyer_id 
FROM   (SELECT s.buyer_id, 
               s.product_id, 
               p.product_name 
        FROM   sales s 
               INNER JOIN product p 
                       ON s.product_id = p.product_id) sp 
GROUP  BY sp.buyer_id 
HAVING Avg(sp.product_name = 'S8') > 0 
       AND Avg(sp.product_name = 'iPhone') = 0; 
