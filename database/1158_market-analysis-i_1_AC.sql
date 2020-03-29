-- https://leetcode.com/problems/market-analysis-i/
-- 1AC, filter, join and group
SELECT u.user_id         buyer_id,
       u.join_date,
       Count(o.order_id) orders_in_2019
FROM   users u
       LEFT JOIN (SELECT order_id,
                         buyer_id,
                         order_date
                  FROM   orders
                  WHERE  order_date BETWEEN {d'2019-01-01'} AND {d'2019-12-31'})
                 o
              ON u.user_id = o.buyer_id
GROUP  BY u.user_id; 
