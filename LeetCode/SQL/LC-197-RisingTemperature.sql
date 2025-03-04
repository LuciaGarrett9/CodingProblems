# Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

CREATE TABLE Weather (
  id int,
  recordDate date,
  temperature int
);

SELECT B.id AS Id
FROM Weather A, Weather B
WHERE A.recordDate = DATE_SUB(B.recordDate, INTERVAL 1 DAY) AND A.temperature < B.temperature;