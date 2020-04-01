-- https://leetcode.com/problems/game-play-analysis-iv/
-- 1AC, complicated
select
  round((
  select
    count(a.player_id) 
  from
    Activity a 
    inner join
      (
        select
          player_id,
          date_add(min(event_date), interval 1 day) sd 
        from
          Activity 
        group by
          player_id
      )
      ad 
      on a.player_id = ad.player_id 
      and a.event_date = ad.sd) / (
      select
        count(distinct player_id) 
      from
        Activity), 2) fraction;
