-- Write your T-SQL query statement below
-- https://www.databasejournal.com/features/mysql/selecting-the-top-n-results-by-group-in-mysql.html
SELECT d.NAME  Department, 
       s2.NAME Employee, 
       s2.salary 
FROM   (SELECT s1.departmentid, 
               s1.NAME, 
               s1.salary 
        FROM  (SELECT NAME, 
                      salary, 
                      departmentid, 
                      Dense_rank() 
                        OVER ( 
                          partition BY departmentid 
                          ORDER BY salary DESC) dr 
               FROM   employee) s1 
        WHERE  s1.dr <= 3) s2 
       INNER JOIN department d 
               ON s2.departmentid = d.id 
ORDER  BY department, 
          s2.salary DESC; 
