-- https://leetcode.com/problems/count-student-number-in-departments/
-- routine
select
  d.dept_name,
  ifnull(sc.cc, 0) student_number 
from
  department d 
  left join
    (
      select
        dept_id,
        count(student_id) cc 
      from
        student 
      group by
        dept_id 
    )
    sc 
    on d.dept_id = sc.dept_id 
order by
  student_number desc,
  d.dept_name;
