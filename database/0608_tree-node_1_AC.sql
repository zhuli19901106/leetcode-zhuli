-- https://leetcode.com/problems/tree-node/
-- switch case
SELECT t.id,
       CASE
         WHEN t.p_id IS NULL THEN 'Root'
         WHEN pc.cc IS NULL THEN 'Leaf'
         ELSE 'Inner'
       end Type
FROM   tree t
       LEFT JOIN (SELECT p_id,
                         Count(id) cc
                  FROM   tree
                  WHERE  p_id IS NOT NULL
                  GROUP  BY p_id) pc
              ON t.id = pc.p_id; 
