-- 15-groups.sql
SELECT score, COUNT(name) as number
FROM second_table
GROUP BY score
ORDER By score DESC;
