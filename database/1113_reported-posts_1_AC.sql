-- https://leetcode.com/problems/reported-posts/ 
-- 1AC
SELECT extra                      report_reason, 
       Count(DISTINCT( post_id )) report_count 
FROM   actions 
WHERE  action_date = {d'2019-07-04'} 
       AND action = 'report' 
GROUP  BY extra; 
