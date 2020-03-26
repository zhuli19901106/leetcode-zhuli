-- https://leetcode.com/problems/queries-quality-and-percentage/    
-- man... wtf
-- Runtime: 355 ms, faster than 99.75% of MySQL online submissions for Queries Quality and Percentage.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Queries Quality and Percentage.
SELECT q.query_name, 
       Round(q.quality, 2) quality, 
       Round(Coalesce(100.0 * pq.cnt_poor_rating / q.cnt_rating, 0), 2) 
                           poor_query_percentage 
FROM   (SELECT query_name, 
               Avg(rating / position) quality, 
               Count(rating)          cnt_rating 
        FROM   queries 
        GROUP  BY query_name) q 
       LEFT JOIN (SELECT query_name, 
                         Count(rating) cnt_poor_rating 
                  FROM   queries 
                  WHERE  rating < 3 
                  GROUP  BY query_name) pq 
              ON q.query_name = pq.query_name; 

