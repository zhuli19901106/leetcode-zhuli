-- https://leetcode.com/problems/nth-highest-salary/
-- stored procedure, from the old tales
CREATE function getnthhighestsalary(n INT)
returns INT
begin
  DECLARE m INT;

  SET m = n - 1;

  RETURN ( SELECT CASE WHEN Count(DISTINCT salary) > m THEN (SELECT DISTINCT(
         salary)
         FROM employee ORDER BY salary DESC LIMIT m, 1) ELSE NULL end FROM
  employee );
end 
