-- https://leetcode.com/problems/game-play-analysis-i/ 
-- 1AC
SELECT `player_id`, 
       Min(`event_date`) "first_login" 
FROM   `activity` 
GROUP  BY `player_id`; 