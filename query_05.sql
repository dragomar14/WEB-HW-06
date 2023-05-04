SELECT t.fullname AS teacher, d.name AS discipline
FROM disciplines d
JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 1
ORDER BY discipline