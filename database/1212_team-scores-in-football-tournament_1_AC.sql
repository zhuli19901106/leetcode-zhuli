-- https://leetcode.com/problems/team-scores-in-football-tournament/ 
-- case, union, join, group and sort 
SELECT t.*, 
       Ifnull(Sum(tp.num_points), 0) num_points 
FROM   teams t 
       LEFT JOIN (SELECT host_team team_id, 
                         CASE 
                           WHEN host_goals > guest_goals THEN 3 
                           WHEN host_goals < guest_goals THEN 0 
                           ELSE 1 
                         end       num_points 
                  FROM   matches 
                  UNION ALL 
                  SELECT guest_team team_id, 
                         CASE 
                           WHEN host_goals > guest_goals THEN 0 
                           WHEN host_goals < guest_goals THEN 3 
                           ELSE 1 
                         end        num_points 
                  FROM   matches) tp 
              ON t.team_id = tp.team_id 
GROUP  BY t.team_id 
ORDER  BY num_points DESC, 
          t.team_id; 
