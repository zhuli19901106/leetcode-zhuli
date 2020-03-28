-- https://leetcode.com/problems/sales-analysis-iii/ 
-- 1AC, use avg() to calculate percentage
SELECT p.product_id, 
       p.product_name 
FROM   product p 
       INNER JOIN (SELECT product_id, 
                          Avg(( sale_date BETWEEN {d'2019-01-01'} AND 
                                                  {d'2019-03-31'} ) 
                                           ) 
                                                      only_spring 
                   FROM   sales 
                   GROUP  BY product_id) os 
               ON p.product_id = os.product_id 
WHERE  os.only_spring = 1; 
