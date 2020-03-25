-- https://leetcode.com/problems/immediate-food-delivery-i/  
-- 1AC, count with primary key
SELECT Round(Count(`delivery_id`) / (SELECT Count(`delivery_id`) 
                                     FROM   `delivery`) * 100.0, 2) 
       "immediate_percentage" 
FROM   `delivery` 
WHERE  `order_date` = `customer_pref_delivery_date`; 