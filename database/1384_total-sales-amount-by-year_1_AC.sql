-- https://leetcode.com/problems/total-sales-amount-by-year/
-- 1AC, now, that's something
select
  r.product_id,
  p.product_name,
  r.report_year,
  r.total_amount 
from
  (
    select
      s.product_id,
      y.report_year,
      case
        when
          period_start > year_end 
          or period_end < year_start 
        then
          0 
        else
(datediff((
          case
            when
              s.period_end < y.year_end 
            then
              s.period_end 
            else
              y.year_end 
          end
), 
          (
            case
              when
                s.period_start > y.year_start 
              then
                s.period_start 
              else
                y.year_start 
            end
          )
) + 1) * s.average_daily_sales 
      end
      total_amount 
    from
      Sales s 
      cross join
        (
          select
            "2018" report_year,
            {d'2018-01-01'} year_start,
            {d'2018-12-31'} year_end 
          union all
          select
            "2019",
            {d'2019-01-01'} year_start,
            {d'2019-12-31'} year_end 
          union all
          select
            "2020",
            {d'2020-01-01'} year_start,
            {d'2020-12-31'} year_end
        )
        y
  )
  r 
  inner join
    Product p 
    on r.product_id = p.product_id 
where
  r.total_amount > 0 
order by
  r.product_id,
  r.report_year;
