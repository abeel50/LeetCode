# Write your MySQL query statement below
select 
    max(u.name) name,
    ifnull(sum(distance),0) travelled_distance
from Users u left join Rides r
on r.user_id = u.id 
group by u.id
order by 2 desc, 1