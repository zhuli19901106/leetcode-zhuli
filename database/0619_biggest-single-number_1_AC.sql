-- https://leetcode.com/problems/biggest-single-number/ 
-- 1AC
SELECT Max(un.num) num 
FROM   (SELECT num 
        FROM   my_numbers 
        GROUP  BY num 
        HAVING Count(num) = 1) un; 
