# Write your MySQL query statement below
Select res.Department, res.Employee, res.Salary
from (
    Select 
        D.name as Department,
        E.Name as Employee,
        E.salary as Salary,
        dense_rank() over (partition by D.name order by E.salary desc) as rnk
    from
        Employee as E
    inner join
        Department as D on E.departmentId = D.id
) as res
where res.rnk = 1;