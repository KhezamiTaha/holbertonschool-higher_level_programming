-- 14-my_genres.sql
SELECT tv_genres.name
FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.id = (
    SELECT tv_shows.id
    FROM tv_shows
    WHERE title = "Dexter")
ORDER BY name;
