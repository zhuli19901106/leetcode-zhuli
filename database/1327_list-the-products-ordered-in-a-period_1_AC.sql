-- https://leetcode.com/problems/list-the-products-ordered-in-a-period/ 
-- 1AC
SELECT p.product_name PRODUCT_NAME, 
       og.su          UNIT 
FROM   products p 
       INNER JOIN (SELECT product_id, 
                          Sum(unit) su 
                   FROM   orders 
                   WHERE  order_date >= {d'2020-02-01'} 
                          AND order_date <= {d'2020-02-29'} 
                   GROUP  BY product_id 
                   HAVING su >= 100) og 
               ON p.product_id = og.product_id; 
