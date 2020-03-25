-- https://leetcode.com/problems/find-the-team-size/ 
-- 1AC
SELECT e.`employee_id`, 
       ts.`team_size` 
FROM   `employee` e 
       INNER JOIN (SELECT `team_id`, 
                          Count(`employee_id`) "team_size" 
                   FROM   `employee` 
                   GROUP  BY `team_id`) ts 
               ON e.`team_id` = ts.`team_id`; 