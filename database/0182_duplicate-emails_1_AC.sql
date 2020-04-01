-- https://leetcode.com/problems/duplicate-emails/ 
-- 1AC
SELECT email 
FROM   person 
GROUP  BY email 
HAVING Count(email) > 1; 
