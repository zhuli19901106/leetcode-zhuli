-- https://leetcode.com/problems/game-play-analysis-ii/  
-- not very clean
SELECT DISTINCT a.player_id, 
                a.device_id 
FROM   activity a 
       INNER JOIN (SELECT player_id, 
                          Min(event_date) event_date 
                   FROM   activity 
                   GROUP  BY player_id) amd 
               ON a.player_id = amd.player_id 
WHERE  a.event_date = amd.event_date; 
