-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
-- 1AC, first SQL question
select e.`unique_id`, e.`name` from `Employees` e left join `EmployeeUNI` eu on e.`id` == eu.`id`;
