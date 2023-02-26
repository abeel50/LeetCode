# Write your MySQL query statement below
SELECT product_id, 'store1' store, store1 price 
FROM Products
where store1 is not null
union
SELECT product_id, 'store2' store, store2 price 
FROM Products
where store2 is not null
union
SELECT product_id, 'store3' store, store3 price 
FROM Products
where store3 is not null;