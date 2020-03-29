-- https://leetcode.com/problems/active-businesses/
-- 1AC
SELECT e.business_id 
FROM   events e 
       INNER JOIN (SELECT event_type, 
                          Avg(occurences) avg_occurences 
                   FROM   events 
                   GROUP  BY event_type) ec 
               ON e.event_type = ec.event_type 
                  AND e.occurences > ec.avg_occurences 
GROUP  BY e.business_id 
HAVING Count(e.event_type) > 1; 
