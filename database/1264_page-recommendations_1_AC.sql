-- https://leetcode.com/problems/page-recommendations/ 
-- 1AC, not quite efficient, but OK
SELECT DISTINCT( page_id ) recommended_page 
FROM   likes 
WHERE  user_id IN (SELECT user2_id 
                   FROM   friendship 
                   WHERE  user1_id = 1 
                   UNION 
                   SELECT user1_id 
                   FROM   friendship 
                   WHERE  user2_id = 1) 
       AND page_id NOT IN (SELECT page_id 
                           FROM   likes 
                           WHERE  user_id = 1) 
ORDER  BY recommended_page; 
