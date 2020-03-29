-- https://leetcode.com/problems/highest-grade-for-each-student/ 
-- filter at join 
SELECT e.student_id, 
       Min(e.course_id) course_id, 
       e.grade 
FROM   enrollments e 
       INNER JOIN (SELECT student_id, 
                          Max(grade) max_grade 
                   FROM   enrollments 
                   GROUP  BY student_id) eg 
               ON e.student_id = eg.student_id 
                  AND e.grade = eg.max_grade 
GROUP  BY e.student_id 
ORDER  BY e.student_id; 
