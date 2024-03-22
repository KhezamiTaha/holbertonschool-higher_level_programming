-- 9-cities_by_state_join.sql
SELECT *
FROM cities JOIN states
    ON cities.state_id = states.id
ORDER BY cities.id ASC;
