-- https://leetcode.com/problems/sales-analysis-i/ 
-- 1AC, user variable is disabled
SELECT seller_id 
FROM   sales 
GROUP  BY seller_id 
HAVING Sum(price) = (SELECT Sum(price) sp 
                     FROM   sales 
                     GROUP  BY seller_id 
                     ORDER  BY sp DESC 
                     LIMIT  1); 
