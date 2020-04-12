-- https://leetcode.com/explore/interview/card/apple/348/others/2035/
-- 1AC, dense_rank exactly
select
  score,
  dense_rank() over (
order by
  score desc) rank 
from
  scores;
