-- https://leetcode.com/problems/product-sales-analysis-iii/
-- 1AC, group and join
select
  s.product_id,
  spy.first_year,
  s.quantity,
  s.price 
from
  Sales s 
  inner join
    (
      select
        product_id,
        min(year) first_year 
      from
        Sales 
      group by
        product_id
    )
    spy 
    on s.product_id = spy.product_id 
    and s.year = spy.first_year;
