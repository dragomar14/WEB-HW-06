SELECT t.fullname AS teacher, d.name AS discipline, ROUND(AVG(g.grade), 2) AS avg_grade
FROM teachers t
JOIN grades g ON g.discipline_id = d.id
JOIN disciplines d ON d.teacher_id = t.id
WHERE t.id = 2
GROUP BY discipline
ORDER BY discipline