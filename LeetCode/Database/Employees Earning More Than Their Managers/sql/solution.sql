-- select b.name as Employee from Employee a
-- join Employee b
-- on a.id = b.managerId
-- where b.salary > a.salary;

select a.name as Employee from Employee a
join Employee b
on b.id = a.managerId
where a.salary > b.salary;