-- https://leetcode.com/problems/shortest-distance-in-a-line/ 
-- 1AC, SQL Server lag function
SELECT   x - Lag(x, 1) over (ORDER BY x) shortest 
FROM     point 
ORDER BY shortest 
offset   1 rows 
FETCH next 1 rows only;