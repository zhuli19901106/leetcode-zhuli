-- https://leetcode.com/problems/weather-type-in-each-country/ 
-- 1AC
SELECT c.country_name, 
       sw.weather_type 
FROM   countries c 
       RIGHT JOIN (SELECT country_id, 
                          CASE 
                            WHEN Avg(weather_state) <= 15 THEN 'Cold' 
                            WHEN Avg(weather_state) >= 25 THEN 'Hot' 
                            ELSE 'Warm' 
                          END weather_type 
                   FROM   weather 
                   WHERE  day BETWEEN {d'2019-11-01'} AND {d'2019-11-30'} 
                   GROUP  BY country_id) sw 
               ON c.country_id = sw.country_id; 
