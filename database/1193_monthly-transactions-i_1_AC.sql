-- https://leetcode.com/problems/monthly-transactions-i/ 
-- 1AC, use case when to avoid extra join or union
SELECT tm.month, 
       tm.country, 
       Count(tm.id)            trans_count, 
       Sum(tm.approved)        approved_count, 
       Sum(tm.amount)          trans_total_amount, 
       Sum(tm.approved_amount) approved_total_amount 
FROM   (SELECT t.*, 
               Date_format(trans_date, '%Y-%m') month, 
               CASE 
                 WHEN state = 'approved' THEN 1 
                 ELSE 0 
               end                              approved, 
               CASE 
                 WHEN state = 'approved' THEN amount 
                 ELSE 0 
               end                              approved_amount 
        FROM   transactions t) tm 
GROUP  BY tm.country, 
          tm.month 
ORDER  BY tm.month; 
