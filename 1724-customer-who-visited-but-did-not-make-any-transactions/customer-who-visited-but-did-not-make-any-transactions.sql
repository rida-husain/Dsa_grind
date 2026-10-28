# Write your MySQL query statement below

-- select visits.visit_id,visists.custoemr_id
-- from visits
-- union transaction 
-- where t.transaction_id  = null

select v.customer_id, count(v.visit_id) as count_no_trans
from visits v
left join transactions t
 on v.visit_id = t.visit_id
 where t.transaction_id is null
 group by v.customer_id;



