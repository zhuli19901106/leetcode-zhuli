-- https://leetcode.com/problems/students-with-invalid-departments/ 
-- 1AC
SELECT dt.`id`, 
       dt.`name` 
FROM   (SELECT d.`id` AS did, 
               s.`id`, 
               s.`name` 
        FROM   `students` s 
               LEFT JOIN `departments` d 
                      ON s.`department_id` = d.`id` 
        WHERE  d.`id` IS NULL) dt; 