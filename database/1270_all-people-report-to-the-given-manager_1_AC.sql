-- https://leetcode.com/problems/all-people-report-to-the-given-manager/ 
-- 1AC, what? I thought the case was gonna be more rigorous.
SELECT employee_id 
FROM   employees 
WHERE  manager_id IN (SELECT employee_id 
                      FROM   employees 
                      WHERE  manager_id IN (SELECT employee_id 
                                            FROM   employees 
                                            WHERE  manager_id IN ( 1 ))) 
       AND employee_id != 1; 
