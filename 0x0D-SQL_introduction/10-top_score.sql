-- Script to print out name and score
-- showing the highest score first

SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
