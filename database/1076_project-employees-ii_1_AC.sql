-- https://leetcode.com/problems/project-employees-ii/ 
-- 1AC, max count
SELECT project_id 
FROM   project 
GROUP  BY project_id 
HAVING Count(employee_id) = (SELECT Count(employee_id) ec 
                             FROM   project 
                             GROUP  BY project_id 
                             ORDER  BY ec DESC 
                             LIMIT  1); 
