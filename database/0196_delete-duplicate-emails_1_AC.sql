-- https://leetcode.com/problems/delete-duplicate-emails/ 
-- 1AC, table must be copied so as to query and delete at the same time
DELETE FROM person 
WHERE  id NOT IN (SELECT Min(p.id) 
                  FROM   (SELECT * 
                          FROM   person) p 
                  GROUP  BY p.email); 
