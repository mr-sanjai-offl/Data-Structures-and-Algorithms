# Write your MySQL query statement belo
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(class) > 4;