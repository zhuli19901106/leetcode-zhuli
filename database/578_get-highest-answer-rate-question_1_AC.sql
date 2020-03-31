-- https://leetcode.com/problems/get-highest-answer-rate-question/
-- 1AC, quite the number of downvotes
select
  question_id survey_log 
from
  survey_log 
group by
  question_id 
order by
  sum(action = 'answer') / sum(action = 'show') desc limit 1;
