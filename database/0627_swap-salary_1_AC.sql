-- https://leetcode.com/problems/swap-salary/ 
-- 1AC, case statement
UPDATE salary 
SET    sex = CASE sex 
               WHEN 'm' THEN 'f' 
               WHEN 'f' THEN 'm' 
             end; 
