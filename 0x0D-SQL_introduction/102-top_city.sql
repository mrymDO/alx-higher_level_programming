-- Displays Top 3 of cities temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month(date) IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
