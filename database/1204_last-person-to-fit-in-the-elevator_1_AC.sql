-- https://leetcode.com/problems/last-person-to-fit-in-the-elevator/
-- 1AC, prefix sum
SELECT psw.person_name 
FROM   (SELECT q1.person_name, 
               q1.turn, 
               Sum(q2.weight) sum_weight 
        FROM   queue q1 
               INNER JOIN queue q2 
                       ON q2.turn <= q1.turn 
        GROUP  BY q1.person_id 
        ORDER  BY q1.turn) psw 
WHERE  psw.sum_weight <= 1000 
ORDER  BY psw.turn DESC 
LIMIT  1; 
