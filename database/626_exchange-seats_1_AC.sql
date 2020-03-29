-- https://leetcode.com/problems/exchange-seats/
-- SQL Server solution, simple idea but lots of writing.
SELECT id,
       CASE
         WHEN ( id - 1 ) / 2 = ( Lead(id)
                                   OVER(
                                     ORDER BY id) - 1 ) / 2 THEN Lead(student)
         OVER(
           ORDER BY id)
         WHEN ( id - 1 ) / 2 = ( Lag(id)
                                   OVER(
                                     ORDER BY id) - 1 ) / 2 THEN Lag(student)
         OVER(
           ORDER BY id)
         ELSE student
       END student
FROM   seat; 
