-- https://leetcode.com/problems/unpopular-books/
-- description is a bit ambiguous
select
  b.book_id,
  b.name 
from
  (
    select
      book_id,
      name 
    from
      Books 
    where
      datediff({d'2019-06-23'}, available_from) >= 30
  )
  b 
  left join
    (
      select
        book_id,
        sum(quantity) quantity 
      from
        Orders 
      where
        dispatch_date > {d'2018-06-23'} 
      group by
        book_id
    )
    o 
    on b.book_id = o.book_id 
where
  o.quantity is null 
  or o.quantity < 10;
