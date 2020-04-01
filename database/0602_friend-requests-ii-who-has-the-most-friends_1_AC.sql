-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
-- 1AC, straightforward
select
  f.id,
  count(f.id) num 
from
  (
    select
      requester_id id 
    from
      request_accepted 
    union all
    select
      accepter_id id 
    from
      request_accepted
  )
  f 
group by
  f.id 
order by
  num desc limit 1;
