-- https://leetcode.com/problems/new-users-daily-count/
-- group and group
select
  ul.login_date,
  count(ul.user_id) user_count 
from
  (
    select
      user_id,
      min(activity_date) login_date 
    from
      Traffic 
    where
      activity = 'login' 
    group by
      user_id
  )
  ul 
where
  datediff({d'2019-06-30'}, ul.login_date) between 0 and 90 
group by
  ul.login_date;
