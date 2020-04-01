-- https://leetcode.com/problems/triangle-judgement/ 
-- 1AC, a + b > c 
SELECT *, 
       CASE 
         WHEN Least(x, y, z) + ( x + y + z - Least(x, y, z) - Greatest(x, y, z) 
                               ) > 
              Greatest(x, y, z) THEN 'Yes' 
         ELSE 'No' 
       end triangle 
FROM   triangle; 
