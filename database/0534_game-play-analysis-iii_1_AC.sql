-- https://leetcode.com/problems/game-play-analysis-iii/ 
-- 1AC, order by and prefix sum
SELECT a1.player_id, 
       a1.event_date, 
       Sum(a2.games_played) games_played_so_far 
FROM   activity a1 
       INNER JOIN activity a2 
               ON a1.player_id = a2.player_id 
                  AND a2.event_date <= a1.event_date 
GROUP  BY a1.player_id, 
          a1.event_date 
ORDER  BY a1.player_id, 
          a1.event_date; 
