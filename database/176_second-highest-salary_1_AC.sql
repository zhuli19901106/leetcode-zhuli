-- https://leetcode.com/problems/second-highest-salary/  
-- if else
SELECT IF((SELECT Count(DISTINCT salary) 
           FROM   employee) >= 2, (SELECT salary 
                                   FROM   employee 
                                   ORDER  BY salary DESC 
                                   LIMIT  1, 1), NULL) SecondHighestSalary; 
