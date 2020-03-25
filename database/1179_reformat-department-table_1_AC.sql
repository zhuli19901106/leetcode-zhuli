-- https://leetcode.com/problems/reformat-department-table/ 
-- 1AC, pivot table 
SELECT `id`, 
       Sum(CASE 
             WHEN `month` = "jan" THEN `revenue` 
             ELSE NULL 
           end) "Jan_Revenue", 
       Sum(CASE 
             WHEN `month` = "feb" THEN `revenue` 
             ELSE NULL 
           end) "Feb_Revenue", 
       Sum(CASE 
             WHEN `month` = "mar" THEN `revenue` 
             ELSE NULL 
           end) "Mar_Revenue", 
       Sum(CASE 
             WHEN `month` = "apr" THEN `revenue` 
             ELSE NULL 
           end) "Apr_Revenue", 
       Sum(CASE 
             WHEN `month` = "may" THEN `revenue` 
             ELSE NULL 
           end) "May_Revenue", 
       Sum(CASE 
             WHEN `month` = "jun" THEN `revenue` 
             ELSE NULL 
           end) "Jun_Revenue", 
       Sum(CASE 
             WHEN `month` = "jul" THEN `revenue` 
             ELSE NULL 
           end) "Jul_Revenue", 
       Sum(CASE 
             WHEN `month` = "aug" THEN `revenue` 
             ELSE NULL 
           end) "Aug_Revenue", 
       Sum(CASE 
             WHEN `month` = "sep" THEN `revenue` 
             ELSE NULL 
           end) "Sep_Revenue", 
       Sum(CASE 
             WHEN `month` = "oct" THEN `revenue` 
             ELSE NULL 
           end) "Oct_Revenue", 
       Sum(CASE 
             WHEN `month` = "nov" THEN `revenue` 
             ELSE NULL 
           end) "Nov_Revenue", 
       Sum(CASE 
             WHEN `month` = "dec" THEN `revenue` 
             ELSE NULL 
           end) "Dec_Revenue" 
FROM   `department` 
GROUP  BY `id`; 