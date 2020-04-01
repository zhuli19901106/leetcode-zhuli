-- https://leetcode.com/problems/investments-in-2016/
-- 1AC, not quite efficient, but intuitive,
select
  sum(i.tiv_2016) tiv_2016 
from
  insurance i 
  inner join
    (
      select
        lat,
        lon 
      from
        insurance 
      group by
        lat,
        lon 
      having
        count(*) = 1
    )
    iup 
    on i.lat = iup.lat 
    and i.lon = iup.lon 
where
  tiv_2015 in 
  (
    select
      tiv_2015 
    from
      insurance 
    group by
      tiv_2015 
    having
      count(*) > 1
  )
;
