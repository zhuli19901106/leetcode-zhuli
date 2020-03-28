-- https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/ 
-- not very clean
SELECT Round(Ifnull(Avg(usc.sc), 0), 2) average_sessions_per_user 
FROM   (SELECT Count(DISTINCT session_id) sc 
        FROM   activity 
        WHERE  Datediff({d'2019-07-27'}, activity_date) BETWEEN 0 AND 29 
        GROUP  BY user_id) usc; 
