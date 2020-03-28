-- https://leetcode.com/problems/rising-temperature/ 
-- date add
SELECT w1.id 
FROM   weather w1 
       INNER JOIN weather w2 
               ON Date_add(w1.recorddate, INTERVAL -1 day) = w2.recorddate 
WHERE  w1.temperature > w2.temperature; 
