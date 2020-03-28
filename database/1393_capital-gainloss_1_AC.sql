-- https://leetcode.com/problems/capital-gainloss/
-- 1AC, order by, lag and diff
SELECT s.stock_name, 
       Sum(s.price - s.last_price) capital_gain_loss 
FROM   (SELECT stock_name, 
               price, 
               Lag(price) 
                 OVER ( 
                   ORDER BY stock_name, operation_day) last_price, 
               operation 
        FROM   stocks) s 
WHERE  s.operation = 'Sell' 
GROUP  BY s.stock_name; 
