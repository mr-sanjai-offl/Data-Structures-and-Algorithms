# Write your MySQL query statement below
SELECT E2.name
FROM Employee as E1
INNER JOIN Employee as E2 ON (E1.managerId = E2.id)
GROUP BY E2.id
HAVING COUNT(*) >= 5;