# Write your MySQL query statement below


select 
    a1.machine_id,
    ROUND(AVG(a2.timestamp - a1.timestamp),3) AS processing_time
from activity a1

inner join activity a2

on a1.process_id = a2.process_id
and a1.machine_id = a2.machine_id
AND a1.activity_type = 'start'
AND a2.activity_type = 'end'

group by a1.machine_id;
-- a1 is for start and a2 is for end
-- process_id and machine_id should be same


