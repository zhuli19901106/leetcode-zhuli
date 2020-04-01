-- https://leetcode.com/problems/employees-earning-more-than-their-managers/ 
-- 1AC
SELECT e1.name Employee 
FROM   employee e1 
       INNER JOIN employee e2 
               ON e1.managerid = e2.id 
WHERE  e1.salary > e2.salary; 
