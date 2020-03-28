-- https://leetcode.com/problems/ads-performance/   
-- using avg() for percentage is better
SELECT ad_id, 
       Round(Ifnull(Avg(100 * ( action = 'Clicked' ) / ( action != 'Ignored' )), 
             0), 2) 
       ctr 
FROM   ads 
GROUP  BY ad_id 
ORDER  BY ctr DESC, 
          ad_id; 
