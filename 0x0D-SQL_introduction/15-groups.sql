-- Lists number of record with the same score in second_table
SELECT `score`, COUNT(`score`) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY COUNT(`score`) DESC;
