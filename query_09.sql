SELECT d.name AS discipline, s.fullname AS student
FROM disciplines d
LEFT JOIN students s ON g.student_id = s.id
LEFT JOIN grades g ON g.discipline_id = d.id
WHERE s.id = 5
GROUP BY discipline
ORDER BY discipline