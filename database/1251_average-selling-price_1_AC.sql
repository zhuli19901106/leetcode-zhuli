-- https://leetcode.com/problems/average-selling-price/ 
-- 1AC, now it's getting complicated
SELECT usp.`product_id`, 
       Round(Sum(usp.`revenue`) / Sum(usp.`units`), 2) "average_price" 
FROM   (SELECT us.`product_id`, 
               ( us.`units` * p.`price` ) "revenue", 
               us.`units` 
        FROM   `unitssold` us 
               INNER JOIN `prices` p 
                       ON us.`product_id` = p.`product_id` 
        WHERE  us.`purchase_date` BETWEEN p.`start_date` AND p.`end_date`) usp 
GROUP  BY `product_id`; 