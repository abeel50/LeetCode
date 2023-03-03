# Write your MySQL query statement below
select 
    user_id buyer_id, 
    max(join_date) join_date,
    count(distinct order_id) orders_in_2019
from Users u LEFT JOIN Orders o 
    on u.user_id = o.buyer_id and LEFT(order_date,4)='2019'
group by 1