# Write your MySQL query statement below
select res.Department, res.Employee, res.Salary
from(
    select 
        Department.name as Department,
        Employee.name as Employee, 
        Employee.salary as Salary, 
        dense_rank() over (partition by Department.name order by Employee.Salary desc) as rnk
    from 
        Employee
    inner join 
        Department on Employee.departmentId = Department.id
) as res
where 
    res.rnk <= 3
order by 
    res.Salary desc, res.Department asc;