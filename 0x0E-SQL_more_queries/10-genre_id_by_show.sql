-- Write a script that lists all shows contained in hbtn_0d_tvshows
-- And that have at least one genre linked.
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
	INNER JOIN `tv_shows_genre` AS g
	ON s.`id` = g.`show_id`
	ORDER BY s.`title`, g.`genre_id`;