SELECT s.fullname AS student, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN students s ON s.id = g.student_id
GROUP BY s.fullname
ORDER BY avg_grade DESC
LIMIT 5;