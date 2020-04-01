-- https://leetcode.com/problems/consecutive-available-seats/
-- 1AC, lag and lead
SELECT cw.seat_id 
FROM   (SELECT seat_id, 
               Lag(seat_id) 
                 OVER ( 
                   ORDER BY seat_id) last_seat_id, 
               Lead(seat_id) 
                 OVER ( 
                   ORDER BY seat_id) next_seat_id 
        FROM   cinema 
        WHERE  free = 1) cw 
WHERE  cw.last_seat_id = cw.seat_id - 1 
        OR cw.next_seat_id = cw.seat_id + 1; 
