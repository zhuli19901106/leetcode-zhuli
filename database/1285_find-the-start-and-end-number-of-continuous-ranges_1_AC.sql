-- https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/ 
-- 1AC, a rather stupid solution
SELECT l1.start_id, 
       Min(l2.end_id) end_id 
FROM   (SELECT log_id start_id 
        FROM   logs 
        WHERE  log_id - 1 NOT IN (SELECT log_id 
                                  FROM   logs)) l1 
       INNER JOIN (SELECT log_id end_id 
                   FROM   logs 
                   WHERE  log_id + 1 NOT IN (SELECT log_id 
                                             FROM   logs)) l2 
               ON l1.start_id <= l2.end_id 
GROUP  BY l1.start_id; 
