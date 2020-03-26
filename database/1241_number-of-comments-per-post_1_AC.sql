-- https://leetcode.com/problems/number-of-comments-per-post/   
SELECT p.post_id, 
       Coalesce(cc.number_of_comments, 0) number_of_comments 
FROM   (SELECT DISTINCT( sub_id ) post_id 
        FROM   submissions 
        WHERE  parent_id IS NULL) p 
       LEFT JOIN (SELECT parent_id, 
                         Count(DISTINCT( sub_id )) number_of_comments 
                  FROM   submissions 
                  WHERE  parent_id IS NOT NULL 
                  GROUP  BY parent_id) cc 
              ON p.post_id = cc.parent_id order by p.post_id; 
