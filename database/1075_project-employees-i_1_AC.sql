-- https://leetcode.com/problems/project-employees-i/ 
-- 1AC
SELECT pe.project_id, 
       Round(Avg(experience_years), 2) average_years 
FROM   (SELECT p.project_id, 
               p.employee_id, 
               e.experience_years 
        FROM   project p 
               LEFT JOIN employee e 
                      ON p.employee_id = e.employee_id) pe 
GROUP  BY pe.project_id; 
