-- https://leetcode.com/problems/activity-participants/
-- 1AC, a bit clumsy
SELECT activity
FROM   friends
GROUP  BY activity
HAVING Count(id) NOT IN (SELECT Min(ac1.ac)
                         FROM   (SELECT Count(id) ac
                                 FROM   friends
                                 GROUP  BY activity) ac1
                         UNION
                         SELECT Max(ac2.ac)
                         FROM   (SELECT Count(id) ac
                                 FROM   friends
                                 GROUP  BY activity) ac2); 
