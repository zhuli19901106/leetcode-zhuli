-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
-- 1AC
SELECT e.name
FROM   employee e
       INNER JOIN (SELECT managerid
                   FROM   employee
                   WHERE  managerid IS NOT NULL
                   GROUP  BY managerid
                   HAVING Count(id) >= 5) m
               ON e.id = m.managerid; 
