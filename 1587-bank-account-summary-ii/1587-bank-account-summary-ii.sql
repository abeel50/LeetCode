# Write your MySQL query statement below
select name, sum(amount) balance
from Users join Transactions using(account)
group by account
having balance >10000