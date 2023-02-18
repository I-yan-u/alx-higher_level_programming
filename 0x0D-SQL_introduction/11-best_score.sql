-- Script to print out name and score
-- showing the highes score first
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
