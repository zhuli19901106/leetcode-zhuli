-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/ 
-- 1AC
SELECT actor_id, 
       director_id 
FROM   actordirector 
GROUP  BY actor_id, 
          director_id 
HAVING Count(timestamp) >= 3; 
