# Write your MySQL query statement below

Select e1.name
from Employee e1
INNER JOIN Employee e2
on e1.id = e2.managerId
GROUP BY e2.managerId
HAVING COUNT(e2.managerId) >= 5;

-- approach since one talbe so inner join
-- then what is common 
-- how to gripu by
-- then count with having condition
