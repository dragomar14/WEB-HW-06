SELECT gr.name AS [group], d.name AS discipline, s.fullname AS student, g.grade AS grade, g.date_of AS date_of
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN groups gr ON gr.id = s.group_id
JOIN disciplines d ON d.id = g.discipline_id
WHERE gr.id = 2 AND d.id = 1
ORDER BY student, date_of