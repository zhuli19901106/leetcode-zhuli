-- https://leetcode.com/problems/rank-scores/
-- 1AC, dense_rank exactly
select
  score,
  dense_rank() over (
order by
  score desc) rank 
from
  scores;
