-- https://leetcode.com/problems/classes-more-than-5-students/  
SELECT class 
FROM   courses 
GROUP  BY class 
HAVING Count(DISTINCT student) >= 5; 
