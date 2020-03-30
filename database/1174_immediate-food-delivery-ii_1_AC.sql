-- https://leetcode.com/problems/immediate-food-delivery-ii/
-- 1AC, avg with condition for percentage
SELECT Round(100 * Avg(d.order_date = d.customer_pref_delivery_date), 2)
       immediate_percentage
FROM   delivery d
       INNER JOIN (SELECT customer_id,
                          Min(order_date) first_order
                   FROM   delivery
                   GROUP  BY customer_id) fo
               ON d.customer_id = fo.customer_id
                  AND d.order_date = fo.first_order; 
