# Write your MySQL query statement below
-- id whose have higher tem pas prev day
-- checking date and temp is greater

select w1.id
-- return id of current day not prev
from weather w1
join weather w2
   on datediff(w1.recordDate, w2.recordDate) = 1

where w1.temperature> w2.temperature;
