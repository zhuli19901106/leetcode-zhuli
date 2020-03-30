-- https://leetcode.com/problems/movie-rating/
-- 1AC, manual labor
( 
SELECT
  u.name results 
FROM
  users u 
  INNER JOIN
    (
      SELECT
        user_id,
        Count(movie_id) rc 
      FROM
        movie_rating 
      GROUP BY
        user_id
    )
    urc 
    ON u.user_id = urc.user_id 
ORDER BY
  urc.rc DESC, u.name LIMIT 1) 
UNION ALL
( 
SELECT
  m.title results 
FROM
  movies m 
  INNER JOIN
    (
      SELECT
        movie_id,
        Avg(rating) ar 
      FROM
        movie_rating 
      WHERE
        created_at BETWEEN {d'2020-02-01'} AND {d'2020-02-29'} 
      GROUP BY
        movie_id
    )
    mar 
    ON m.movie_id = mar.movie_id 
ORDER BY
  mar.ar DESC, m.title LIMIT 1 )
