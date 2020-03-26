-- https://leetcode.com/problems/article-views-i/ 
-- 1AC
-- Runtime: 244 ms, faster than 99.88% of MySQL online submissions for Article Views I. 
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Article Views I. 
SELECT author_id id 
FROM   views 
WHERE  author_id = viewer_id 
GROUP  BY author_id 
HAVING Count(viewer_id) > 0; 
