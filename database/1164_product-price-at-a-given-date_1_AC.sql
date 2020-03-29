-- https://leetcode.com/problems/product-price-at-a-given-date/
-- 1AC, ugly solution
SELECT p.product_id,
       p.new_price price
FROM   products p
       INNER JOIN (SELECT product_id,
                          new_price,
                          Max(change_date) cur_date
                   FROM   products
                   WHERE  change_date <= {d'2019-08-16'}
                   GROUP  BY product_id) pp
               ON p.product_id = pp.product_id
                  AND p.change_date = pp.cur_date
UNION
SELECT product_id,
       10
FROM   products
GROUP  BY product_id
HAVING Min(change_date) > {d'2019-08-16'} 
