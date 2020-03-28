-- https://leetcode.com/problems/project-employees-iii/ 
-- 1AC, bad solution
SELECT pe.project_id, 
       pe.employee_id 
FROM   (SELECT p.project_id, 
               e.employee_id, 
               e.experience_years 
        FROM   project p 
               INNER JOIN employee e 
                       ON p.employee_id = e.employee_id) pe 
       INNER JOIN (SELECT p.project_id, 
                          Max(e.experience_years) max_experience_years 
                   FROM   project p 
                          INNER JOIN employee e 
                                  ON p.employee_id = e.employee_id 
                   GROUP  BY p.project_id) pem 
               ON pe.project_id = pem.project_id 
                  AND pe.experience_years = pem.max_experience_years; 
