# Write your MySQL query statement below
select product_id, product_name
from Sales left join Product using(product_id)
group by 1
having sum(sale_date between '2019-01-01' and '2019-03-31')>0 and 
       sum(sale_date < '2019-01-01' or sale_date > '2019-03-31')=0