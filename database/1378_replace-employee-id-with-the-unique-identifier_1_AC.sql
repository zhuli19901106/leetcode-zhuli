-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/ 
-- 1AC, first SQL question 
SELECT e.`unique_id`, 
       e.`name` 
FROM   `employees` e 
       LEFT JOIN `employeeuni` eu 
              ON e.`id` == eu.`id`; 