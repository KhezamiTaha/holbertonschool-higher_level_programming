-- 11-best_score.sql
SELECT score, name
FROM second_table
where score >= 10
ORDER BY score DESC;
