select *,
case
    when x + y > z
    and x + z > y
    and y + z > x
    then 'Yes'
    else 'No'
end as triangle
from Triangle;
-- Triangle Inequality Theorem: The sum of the lengths of any two sides must be strictly greater than the length of the third side. For sides \(x\), \(y\), and \(z\): \(x + y > z\), \(x + z > y\), and \(y + z > x\)