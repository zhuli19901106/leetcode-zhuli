-- https://leetcode.com/problems/combine-two-tables/ 
-- 1AC
SELECT p.firstname, 
       p.lastname, 
       a.city, 
       a.state 
FROM   person p 
       LEFT JOIN address a 
              ON p.personid = a.personid; 
