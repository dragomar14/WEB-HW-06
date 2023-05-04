SELECT g.name AS [group], s.fullname AS student
FROM students s
JOIN groups g  ON g.id = s.group_id
WHERE g.id = 3
ORDER BY student