-- ---------------------------------------------------------
-- MODULE 04: SQL JOINS AND SUBQUERIES
-- Topics: TYPES OF SQL JOINS (INNER,LEFT RIGHT)- 2TABLE KO JODNA
-- 👤 AUTHOR: Maaz Usmani
-- ---------------------------------------------------------

--join combines the rows between multi table with the help of common column between them 
--it does not insert the rows i just
--there are 7 types of joints
--1. inner joi
--2. left join
--3. right join
--4.full join
--5. self join
--6. naturl join
--7. cross join

--the first three the basic join where the remaining joins are intermediate and advance level join.
--in the place of inner join i can right normally join
--also,beacause inner join is the by default join in my sql.




show tables;
CREATE TABLE Employees_8 (
    Employee_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50)
);

INSERT INTO Employees_8 (Employee_ID, Name, Department) VALUES
(1, 'Aakash', 'HR'),
(2, 'Priya', 'IT'),
(3, 'Rahul', 'Sales'),
(4, 'Sita', 'IT');



CREATE TABLE Salaries (
    Employee_ID INT,
    Salary INT
);

INSERT INTO Salaries (Employee_ID, Salary) VALUES
(1, 50000),
(2, 70000),
(3, 60000),
(5, 80000);


select * from employees_8;
select * from salaries;


select  E.Employee_id,S.Salary
from employees_8 as E
inner join
salaries as S
on E.Employee_id=S.Employee_id;


select  E.Employee_id,S.Salary
from employees_8 as E
left join
salaries as S
on E.Employee_id=S.Employee_id;

select  E.Employee_id,S.Salary
from employees_8 as E
right join
salaries as S
on E.Employee_id=S.Employee_id;












-- ---------------------------------------------------------
--n PRACTICE FOR JOINS FROM DIFFRENT TABLE
-- ---------------------------------------------------------


create database joint;
use joint;
CREATE TABLE employees_null_practice (
emp_id INT,
emp_name VARCHAR(50),
department VARCHAR(50),
salary INT,
bonus INT,
manager_id INT
);

INSERT INTO employees_null_practice VALUES
(1, 'Amit', 'IT', 50000, 5000, NULL),
(2, 'Rahul', 'HR', NULL, 3000, 1),
(3, 'Sita', NULL, 45000, NULL, 1),
(4, 'Neha', 'Finance', 60000, NULL, 2),
(5, 'Vikas', 'IT', NULL, 4000, 2),
(6, 'Priya', NULL, 52000, 3500, 3),
(7, 'Ankit', 'HR', 48000, NULL, NULL),
(8, 'Pooja', 'Finance', NULL, 2000, 4),
(9, 'Rohit', NULL, 55000, NULL, NULL),
(10, 'Sneha', 'IT', NULL, NULL, 5);

use  joint;
show tables;

select * from null_practice;

select *, isnull(department)
from 
null_practice;

select * ,ifnull(department,2)
from 
null_practice;

-- there if null is replace by colesce for putting multiple cond.
select * ,coalesce(department,bonous,100)
from null_practice;

-- for chechkinf the presence of null we use isnull and for replacing the null by any value in the new column we use if null otherwise collesce

create database inner_join;



-- Customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO customers VALUES
(1,'Shubham','Delhi','shubham@gmail.com'),
(2,'Amit','Mumbai','amit@gmail.com'),
(3,'Neha','Pune','neha@gmail.com'),
(4,'Rohit','Delhi','rohit@gmail.com'),
(5,'Priya','Bangalore','priya@gmail.com');

select * from customers;

-- Categories table
CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(50)
);

INSERT INTO categories VALUES
(1,'Electronics'),
(2,'Clothing'),
(3,'Books');
 
 select * from categories;
-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price DECIMAL(10,2),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

INSERT INTO products VALUES
(101,'Laptop',50000,1),
(102,'Mobile',20000,1),
(103,'T-Shirt',500,2),
(104,'Jeans',1200,2),
(105,'SQL Book',700,3);

select * from products;
-- Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders VALUES
(1001,1,'2024-01-10'),
(1002,2,'2024-01-12'),
(1003,1,'2024-01-15'),
(1004,3,'2024-01-18'),
(1005,5,'2024-01-20');
 select * from orders;
-- Order Items table
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO order_items VALUES
(1,1001,101,1),
(2,1001,103,2),
(3,1002,102,1),
(4,1003,105,3),
(5,1004,104,1),
(6,1005,101,1);

select * from order_items;
-- SAMPLE JOIN QUERY
SELECT customers.customer_name, products.product_name, order_items.quantity
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
JOIN order_items ON orders.order_id = order_items.order_id
JOIN products ON order_items.product_id = products.product_id;

select * from
categories as c
inner join
products as p
on
c.category_id=p.category_id;


select category_id,product_name,price







-- ---------------------------------------------------------
-- Topics: CROSS JOIN
-- ---------------------------------------------------------

 CREATE TABLE employee ( employee_id INT PRIMARY
KEY, employee_name VARCHAR(50), job_title VARCHAR(50), manager_id INT,
salary INT );

INSERT INTO employee VALUES (1, 'Amit', 'CEO', NULL,
100000); INSERT INTO employee VALUES (2, 'Neha', 'Manager', 1, 75000);
INSERT INTO employee VALUES (3, 'Raj', 'Manager', 1, 72000); INSERT INTO
employee VALUES (4, 'Priya', 'Team Lead', 2, 60000); INSERT INTO
employee VALUES (5, 'Vikas', 'Team Lead', 2, 58000); INSERT INTO
employee VALUES (6, 'Sneha', 'Developer', 4, 45000); INSERT INTO
employee VALUES (7, 'Arjun', 'Developer', 4, 43000); INSERT INTO
employee VALUES (8, 'Kavita', 'Developer', 5, 42000); INSERT INTO
employee VALUES (9, 'Rohit', 'Intern', 6, 25000); INSERT INTO employee
VALUES (10, 'Pooja', 'Intern', 7, 24000); INSERT INTO employee VALUES
(11, 'Manish', 'HR', 2, 50000); INSERT INTO employee VALUES (12,
'Simran', 'Accountant', 3, 52000);



select * from employee; 

select * from employyee;
select e.employee_name as employee_name,
m.employee_name as manager_name
from 
employee as e
inner join
employee as m
on
e.manager_id=m.employee_id;

-- cross join
select * from 
categories
cross join
customers;


-- natural join
select * from 
categories
natural join
products;

/* self join:-it can be defined as the taable perform the join with itself

cross join: it gives the cartesian product 


natural join; it finds the common coloumn between the tables by it self 
if there is a common column them it will be provide the inner join and if its 
not there them it provides cross join means certesian 
product so it also doesnt require the "on" condition*/

































































