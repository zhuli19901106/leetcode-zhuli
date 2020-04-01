-- https://leetcode.com/problems/shortest-distance-in-a-plane/
-- 1AC, math ops
SELECT Round(Min(Sqrt(Pow(p1.x - p2.x, 2) + Pow(p1.y - p2.y, 2))), 2) shortest
FROM   point_2d p1
       INNER JOIN point_2d p2
               ON p1.x != p2.x
                   OR p1.y != p2.y; 
