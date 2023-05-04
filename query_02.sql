SELECT d.name AS discipline, s.fullname AS student, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id
WHERE d.id = 3
GROUP BY s.fullname
ORDER BY avg_grade DESC
LIMIT 1;