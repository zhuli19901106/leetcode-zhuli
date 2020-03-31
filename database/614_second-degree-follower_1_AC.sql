-- https://leetcode.com/problems/second-degree-follower/
-- too sloppy
select distinct
  followee follower,
  count(distinct follower) num 
from
  follow 
where
  followee in 
  (
    select
      follower 
    from
      follow
  )
group by
  followee 
order by
  followee;
