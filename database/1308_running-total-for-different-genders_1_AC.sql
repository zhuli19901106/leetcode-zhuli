-- https://leetcode.com/problems/running-total-for-different-genders/
-- 1AC, that feels dizzy
SELECT s1.gender, 
       s1.day, 
       Sum(s2.score_points) total 
FROM   scores s1 
       INNER JOIN (SELECT gender, 
                          day, 
                          score_points 
                   FROM   scores 
                   -- WHERE  gender = 'F'  
                   ORDER  BY gender, 
                             day) s2 
               ON s2.gender = s1.gender 
                  AND s2.day <= s1.day 
GROUP  BY s1.gender, 
          s1.day; 
