-- ---------------------------------------------------------
-- MODULE 03: FILTERING AND SORTING DATA
-- Topics: ORDER BY, LIMIT, OFFSET, and WHERE Clause
-- 👤 AUTHOR: Maaz Usmani
-- ---------------------------------------------------------

-- 1. Sorting data by salary (Highest to Lowest)
SELECT * FROM sales
ORDER BY price DESC;

-- 2. Using LIMIT to get Top 5 records
SELECT * FROM sales
LIMIT 5;

-- 3. Using OFFSET to skip records (Paging)
SELECT * FROM sales
LIMIT 5 OFFSET 5;


select * from sales;
-- we using order by clause to arrange the data in asc or desc price wise
select * from sales order by price;
select * from sales order by price desc;

-- now we using limit clause to limit the rows
select * from sales limit 4;
select * from sales order by price desc limit 3;

/* short trick to remember the sequence
FROM 
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT
OFFSET


-- now we want the earlier case only but we want to skip the first row
select * from sales order by price desc limit 3 offset 1;

-- where clause is use for the filter process
-- order by clause is use for sorting the data
-- limit clause is used to see the top or bottom n number of rows

select * from sales order by price desc limit3;

/* every rdms can be dbms 
reasom because data must betabular formaat sql langauage is used tomanaged the data 
but every dbms cant be rdms
in dbms data can be in tabular can be used to manged data */

select city from sales;






-- ---------------------------------------------------------
-- MODULE 04: ADVANCED FILTERING OPERATORS
-- Topics: BETWEEN, IN, and LIKE (Pattern Matching)
-- ---------------------------------------------------------

-- 1. Using BETWEEN to find a range (e.g., salary between 20k and 50k)
SELECT * FROM employee 
WHERE salary BETWEEN 20000 AND 50000;

-- 2. Using IN to match multiple specific values
SELECT * FROM employee 
WHERE location IN ('Bhopal', 'Delhi', 'Bihar');

-- 3. Using LIKE for pattern matching (Wildcards)
-- Finds names starting with 'M'
SELECT * FROM sales
WHERE sales_name LIKE 'M%';






-- now we need unique name from the city colimn so we used distrinct keyword
select distinct(city) from sales;


-- membership operator (In Not in)
select * from sales where city in ("mumbai","delhi");

select * from sales where city not in ("mumbai","delhi");


-- renaming the table name



-- add the column profit in sales tables
alter table sales add column profit int;


-- drop the column profit in sales table
alter table sales drop column profit;



-- modify column changing data type
alter table sales modify column price varchar(20);
alter table sales modify column price int;


-- changing the column header name
alter table sales rename column product to prod;
alter table sales rename column prod to product;




/*sql is an decalarative langauge not a procedural language
declarative language means in sql we just tell the needs to the data base that what we want 
but in procedural the complete process is defined step by step
which does't happen in sql*/

select * from sales;


-- truncate is used to superes the table


/* under sql the cmnd are the categories into 5types
 one is DDL
 which works on the structure on the table
 it ccontain the command like 
 1.drop
 2.rename
 3.create
 4.alter 
 5.truncate
 
 shortcut to rename these commands under sql is Dr cat */

 




-- ---------------------------------------------------------
-- NEW PRACTICE SECTION / NEXT TAB START
-- 
-- ---------------------------------------------------------


select * from department;
show tables;
select * from employees;
select * from fees;
SELECT * FROM `orders_dataset.xlsx - orders` LIMIT 10;
set sql_safe_updates=0;
ALTER TABLE `orders_dataset.xlsx - orders` RENAME TO orders;
select * from orders;
select * from orders where city="pune";
select customerName,product from orders;
select distinct city from orders;
select * from orders where category="electronics";
select * from orders where quantity>2;
select city from orders where city in("delhi","pune");
select customername from orders where city="mumbai" and category="electronics";
select * from orders where city in("mumbai","pune");
select * from orders where city in ("Pune", "Mumbai", "Delhi");
select * from orders where city!="bhopal";
select * from orders order by price asc;
select * from orders order by price desc;
select * from orders limit 5;








-- we use it to see the in exixting data base
show tables;
CREATE TABLE sales (
    order_id INT,
    customer_name VARCHAR(50),
    product VARCHAR(50),
    city VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2),
    order_date DATE
);

-- Insert Sample Data (Including NULL Values)
INSERT INTO sales VALUES
(1, 'Amit', 'Laptop', 'Mumbai', 1, 55000, '2024-01-10'),
(2, 'Rahul', 'Mobile', 'Delhi', 2, 20000, '2024-01-12'),
(3, 'Sneha', 'Laptop', 'Mumbai', 1, 60000, '2024-01-15'),
(4, 'Priya', 'Tablet', 'Chennai', 3, 15000, '2024-01-18'),
(5, 'Amit', 'Mobile', 'Mumbai', 1, 18000, '2024-01-20'),
(6, 'Rahul', 'Laptop', 'Delhi', 2, 52000, '2024-01-25'),
(7, 'Sneha', 'Tablet', 'Mumbai', 1, 14000, '2024-01-28'),
(8, 'Priya', 'Mobile', 'Chennai', 2, 21000, '2024-02-02'),
(9, 'Amit', 'Tablet', 'Mumbai', 2, 16000, '2024-02-05'),
(10, 'Rahul', 'Mobile', 'Delhi', 1, 19000, '2024-02-08'),
(11, 'Karan', 'Laptop', 'Mumbai', 1, 58000, '2024-02-10'),
(12, 'Meena', 'Mobile', NULL, 2, 22000, '2024-02-12'),
(13, 'Rohit', NULL, 'Delhi', 1, 30000, '2024-02-15'),
(14, NULL, 'Tablet', 'Chennai', 3, 15000, '2024-02-18'),
(15, 'Anjali', 'Laptop', 'Mumbai', NULL, 62000, '2024-02-20'),
(16, 'Vikas', 'Mobile', 'Delhi', 2, NULL, '2024-02-22'),
(17, 'Neha', 'Tablet', NULL, 1, 14000, NULL),
(18, NULL, NULL, 'Mumbai', 2, 18000, '2024-02-25');


desc sales;
select * from sales;









-- ---------------------------------------------------------
-- NEW PRACTICE SECTION / NEXT TAB START
-- TOPIC: IS NULL, IS NOT NULL,ORDER BY,
-- ---------------------------------------------------------









-- we using where clausing to filter the table
select * from sales where price>20000;

select * from sales where city="mumbai";
-- we using and operator bcz both the condition are must
select * from sales where city="mumbai" and price>20000;

-- we usijng or operator bcz either condition satisfied than out put come
select * from sales where price>20000 or city="mumbai";
-- we using between operator here to side the limit
select * from sales where price between 25000 and 50000;

-- we using null here 
select * from sales where product is null;

select * from sales where product is not null;
-- for arranging the data in aseending or ddecending we use order by
select * from sales order by price;



--  for arranging the data in aseending or ddecending we use order by
select * from sales order by price desc;
 
-- we useing limke opearator to knoe te names staring with particular letter

select * from sales where customer_name like "a%";



select * from sales where customer_name like "%a";


-- we using under score to fix the posotion
select * from sales where customer_name like "__i%";


select * from sales where customer_name like "a%" and price>30000;




