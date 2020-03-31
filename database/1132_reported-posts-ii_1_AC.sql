-- https://leetcode.com/problems/reported-posts-ii/
-- careful with distinct
select
  round(100 * avg(dp.rem_post_daily / dp.post_daily), 2) average_daily_percent 
from
  (
    select
      count(distinct a.post_id) post_daily,
      count(distinct r.post_id) rem_post_daily 
    from
      Actions a 
      left join
        Removals r 
        on a.post_id = r.post_id 
    where
      action = 'report' 
      and extra = 'spam' 
    group by
      a.action_date
  )
  dp;
