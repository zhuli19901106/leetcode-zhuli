-- https://leetcode.com/problems/restaurant-growth/
-- 1AC, distinct, join, group and order
SELECT c1.visited_on,
       Sum(c2.amount)               amount,
       Round(Sum(c2.amount) / 7, 2) average_amount
FROM   (SELECT DISTINCT visited_on
        FROM   customer) c1
       INNER JOIN customer c2
               ON Datediff(c1.visited_on, c2.visited_on) BETWEEN 0 AND 6
GROUP  BY c1.visited_on
HAVING Count(DISTINCT c2.visited_on) = 7
ORDER  BY c1.visited_on; 
