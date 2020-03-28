-- https://leetcode.com/problems/project-employees-iii/  
-- 1AC, SQL Server dense rank, still slow and clumsy
SELECT pem.project_id, 
       pem.employee_id 
FROM   (SELECT pe.project_id, 
               pe.employee_id, 
               Dense_rank() 
                 OVER( 
                   partition BY pe.project_id 
                   ORDER BY pe.experience_years DESC) rank 
        FROM   (SELECT p.project_id, 
                       p.employee_id, 
                       e.experience_years 
                FROM   project p 
                       INNER JOIN employee e 
                               ON p.employee_id = e.employee_id) pe) pem 
WHERE  pem.rank = 1; 
