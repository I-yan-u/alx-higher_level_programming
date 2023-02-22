-- Write a script that lists all shows contained in hbtn_0d_tvshows
-- That has no genre_id link
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
	LEFT JOIN `tv_shows_genre` AS g
	ON s.`id` = g.`show_id`
	WHERE g.`genre_id` IS NULL
	ORDER BY s.`title`, g.`genre_id`;
