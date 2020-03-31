-- https://leetcode.com/problems/monthly-transactions-ii/
-- WTF is this?
select
  coalesce(cma.month, cmc.month) month,
  coalesce(cma.country, cmc.country) country,
  coalesce(cma.approved_count, 0) approved_count,
  coalesce(cma.approved_amount, 0) approved_amount,
  coalesce(cmc.chargeback_count, 0) chargeback_count,
  coalesce(cmc.chargeback_amount, 0) chargeback_amount 
from
  (
    SELECT
      tm.month,
      tm.country,
      Sum(tm.approved) approved_count,
      Sum(tm.approved_amount) approved_amount 
    FROM
      (
        SELECT
          t.*,
          convert(varchar(7), trans_date, 126) month,
          CASE
            WHEN
              state = 'approved' 
            THEN
              1 
            ELSE
              0 
          end
          approved, 
          CASE
            WHEN
              state = 'approved' 
            THEN
              amount 
            ELSE
              0 
          end
          approved_amount 
        FROM
          transactions t
      )
      tm 
    GROUP BY
      tm.country, tm.month
  )
  cma 
  full outer join
    (
      select
        cm.month,
        cm.country,
        count(cm.chargeback_amount) chargeback_count,
        sum(cm.chargeback_amount) chargeback_amount 
      from
        (
          select
            convert(varchar(7), c.trans_date, 126) month,
            t.country,
            t.id,
            t.amount chargeback_amount 
          from
            Transactions t 
            inner join
              Chargebacks c 
              on t.id = c.trans_id
        )
        cm 
      group by
        cm.country,
        cm.month
    )
    cmc 
    on cma.month = cmc.month 
    and cma.country = cmc.country 
where
  approved_count > 0 
  or approved_amount > 0 
  or chargeback_count > 0 
  or chargeback_amount > 0 
order by
  month;
