-- https://leetcode.com/problems/product-sales-analysis-ii/ 
-- 1AC
SELECT `product_id`, 
       Sum(`quantity`) "total_quantity" 
FROM   `sales` 
GROUP  BY `product_id`; 