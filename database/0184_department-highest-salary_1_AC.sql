-- https://leetcode.com/problems/department-highest-salary/
-- 1AC, join join join
select
  d.Name Department,
  hs.Name Employee,
  hs.Salary 
from
  Department d 
  inner join
    (
      select
        e.DepartmentId,
        e.Name,
        e.Salary 
      from
        Employee e 
        inner join
          (
            select
              DepartmentId,
              max(Salary) Salary 
            from
              Employee 
            group by
              DepartmentId
          )
          ds 
          on e.DepartmentId = ds.DepartmentId 
          and e.Salary = ds.Salary
    )
    hs 
    on d.Id = hs.DepartmentId;
