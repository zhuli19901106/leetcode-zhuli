-- https://leetcode.com/problems/winning-candidate/
-- 1AC
select
  c.Name 
from
  Candidate c 
  inner join
    (
      select
        CandidateId,
        count(CandidateId) cc 
      from
        Vote 
      group by
        CandidateId
    )
    vc 
    on c.id = vc.CandidateId 
order by
  vc.cc desc limit 1;
