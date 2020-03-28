-- https://leetcode.com/problems/ads-performance/  
-- well, that's not a clean solution.
SELECT aaa.ad_id, 
       Round(CASE 
               WHEN aaa.cc + aaa.vc > 0 THEN 100.0 * aaa.cc / ( aaa.cc + aaa.vc 
                                                              ) 
               ELSE 0 
             end, 2) ctr 
FROM   (SELECT aa.ad_id, 
               Sum(aa.cc) cc, 
               Sum(aa.vc) vc 
        FROM   (SELECT ad_id, 
                       CASE 
                         WHEN action = 'Clicked' THEN Count(action) 
                         ELSE 0 
                       end cc, 
                       CASE 
                         WHEN action = 'Viewed' THEN Count(action) 
                         ELSE 0 
                       end vc 
                FROM   ads 
                GROUP  BY ad_id, 
                          action) aa 
        GROUP  BY aa.ad_id) aaa 
ORDER  BY ctr DESC, 
          ad_id; 
