-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/ 
-- 1AC
SELECT activity_date              day, 
       Count(DISTINCT( user_id )) active_users 
FROM   activity 
WHERE  Datediff({d'2019-07-27'}, activity_date) BETWEEN 0 AND 29 
GROUP  BY activity_date; 
