-- https://leetcode.com/problems/find-customer-referee/ 
-- 1AC
SELECT name 
FROM   customer 
WHERE  referee_id != 2 
        OR referee_id IS NULL; 
