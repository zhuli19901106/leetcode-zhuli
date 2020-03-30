-- https://leetcode.com/problems/consecutive-numbers/
-- 1AC, lag and lag
select distinct
(lcs.num) ConsecutiveNums 
from
  (
    select
      id,
      num,
      case
        when
          num = lag(num) over (
    order by
      id) 
    then
      lag(cnt) over (
    order by
      id) + 2 
    else
      1 
      end
      cntsum 
    from
      (
        select
          id,
          num,
          case
            when
              num = lag(num) over (
        order by
          id) 
        then
          1 
        else
          0 
          end
          cnt 
        from
          logs
      )
      lc
  )
  lcs 
where
  lcs.cntsum >= 3;
