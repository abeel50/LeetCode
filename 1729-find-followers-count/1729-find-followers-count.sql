# Write your MySQL query statement below
select user_id, count(follower_id) followers_count
from Followers
group by 1
order by 1