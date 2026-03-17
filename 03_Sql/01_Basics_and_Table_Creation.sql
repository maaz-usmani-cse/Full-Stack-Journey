
-- Module 01: Basics and Table Creation
-- Practice from Workbench Tabs 1 to 10
-- 👤 AUTHOR: Maaz Usmani





-- first class (single line comment)
create database company;
use company;

-- now we creating table under the company database
create table employee 
(e_id int,
e_name varchar(20),
e_performance varchar(20),
e_salary int,
e_joining_date date
);


-- too see the detail of employee table
desc employee;

-- now we insert in the table
insert into employee(e_id,e_name,e_performance,e_salary,e_joining_date)
values
(1,"aa","good",10000,"2020-01-01"),
(2,"bb","bad",20000,"2020-01-01"),
(3,"cc","average",30000,"2020-01-01");


-- how to write multi line cmnts
-- answer for single line i use -- or ##


/* for multi line we use  /* and then
 writting the multi lines and then
 closing with */
 
 -- n ow we want to see the compleate created table with data
 select * from employee;
 
 -- for seing particular columns in sql
 select e_name, e_performance from employee;
 

 -- for seing database in whch we working
 select database();
 
 
 -- for deleting any particular table
 drop table employee;
 
 show tables;








-- ---------------------------------------------------------
-- NEW PRACTICE SECTION / NEXT TAB START
-- TOPIC: FIND OUT THE NULL VALUES
-- ---------------------------------------------------------










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











-- ---------------------------------------------------------
-- NEW PRACTICE SECTION / NEXT TAB START
-- TOPIC:MEMBERSHIP OPERATOR,OFFSET,LIMIT
-- ---------------------------------------------------------







Create database Cybrom;
use cybrom;
create table employee(emp_id int, emp_NAME Varchar(20),salary INT,location varchar(20));
select * from employee;
insert into employee values(1,"Rohit",10000,"Bhopal");
insert into employee values(2,"maaz",20000,"delhi"),(3,"fahad",30000,"delhi"),(4,"sahil",40000,"mumbai"),(5,"faizan",50000,"bihar"),(6,"sonu",60000,"mumbai"),(7,"sarwar",70000,"delhi"),(8,"imran",80000,"nepal"),(9,"maaz",90000,"bihar"),(10,"suraj",1000000,"bhopal");
select emp_NAME,salary from employee;
select emp_NAME from employee where location="bihar";
select * from customer order by salary DESC limit 1 offset 3;
select EmployeeName from customer where department in("hr","it");
select * from customer order by salary DESC limit 1 offset 1;
select count(*) from customer where city="newyork"; 








-- ---------------------------------------------------------
-- MODULE: BASIC DATA AGGREGATION
-- Goal: Learning how to calculate totals and counts from the table
-- ---------------------------------------------------------

-- 1. Counting total records in the table
SELECT COUNT(*) AS total_employees FROM employee2;

-- 2. Calculating total salary expense
SELECT SUM(salary) AS total_salary_budget FROM employee2;





create table employee2(emp_id int, emp_name varchar(20), department varchar(20), salary int, city varchar(20));
 insert into employee2 (emp_id, emp_name, department, salary, city) VALUES
(101, 'Rahul Mehta', 'HR', 55000, 'Mumbai'),
(102, 'Sneha Patel', 'IT', 75000, 'Pune'),
(103, 'Amit Sharma', 'Finance', 62000, 'Delhi'),
(104, 'Neha Singh', 'IT', 82000, 'Mumbai'),
(105, 'Rajat Verma', 'HR', 50000, 'Chennai'),
(106, 'Pooja Das', 'Finance', 72000, 'Pune'),
(107, 'Karan Gupta', 'IT', 88000, 'Delhi'),
(108, 'Deepa Joshi', 'Marketing', 61000, 'Mumbai'),
(109, 'Ravi Kumar', 'HR', 56000, 'Delhi'),
(110, 'Nisha Reddy', 'IT', 70000, 'Hyderabad');
select*from employee2;
select emp_name from employee2 where city="delhi" and salary>80000;
select count(*) from employee2 where department in ("hr","it");
select emp_name from employee2 where department="hr" and city="mumbai";
select emp_name,city from employee2;
select emp_name,department from employee2 where department="hr" and city="mumbai";
select * from employee2 where department="it";
select emp_name,city from employee2;







-- ---------------------------------------------------------
-- NEW PRACTICE SECTION / NEXT TAB START
-- BASIC VERIFICATION (AGGREGATE FUNCTION)
-- ---------------------------------------------------------





select * from customer;
select EmployeeName from customer;
select EmployeeName,salary,city from customer;
select min(salary) from customer;
select max(salary) from customer;
select EmployeeName from customer where employeeid=5;
select EmployeeName, salary,city from customer;
select count(salary) from customer where salary <50000;
select count(salary) from customer where salary <50000;
select sum(salary) from customer;
select EmployeeName, salary*1.2 from customer ;
show tables;
select count(*) from customer where age<35;
select department,sum(salary)from customer group by department;
select * from customer limit 1 offset 2;
select department,sum(salary) from customer group by department order by sum(slary);
select department,max(salary) from customer group by department order by sum(salary);
set sql_safe_updates=0;
update customer set department="hr" where EmployeeID=3;


-- ---------------------------------------------------------
-- NEW PRACTICE SECTION / NEXT TAB START
-- TOPIC: TABLE CONSTARINTS (RULES LAGANA)
-- PRIMARY KEY: DUBLICATE ENTRY NAHI ANE DEGA
-- CHECK:  CONDITION LAGAYEGA (JAISE AGE>18 HE HONE CHAHIYE)
-- ---------------------------------------------------------







/* constraint:
it is used to restriced data whaat data should be allowed into the table 
actually we can conclude tha it has as a filter as a guard
there are 7 types ofconstraints;
1. unique 
2.not null
3.primary key
4.foreign key
5.check 
6.default
7.auto increment*/

create database a;
create table students(
student_id int unique,
student_name varchar(20) not null);

insert into students values
(1,"aa"),
(2,"bb");

select * from students;

-- we learning the use of unique and not null constraint

-- now we learn primary key
-- accutally it is the combination of unique and not null
-- a table the conssist the single primary key only
 create table student1(
 student_id int primary key,
 student_name varchar (20) not null
 );
 
 

 desc student1;
 insert into student1 values
 (1,"aa"),
 (2,"bb");
 
 
 insert into student1 values
 (1,"aa"),
 (2,"bb");
-- now due to primary key the data will not be insert it


 -- now we going to use foreign key
create table order1(
order_id int primary key,
student_id int,
foreign key (student_id) references student1(student_id)
);
 
 
 desc order1;
insert into order1 values
 (1,1),
 (2,2);
 
 -- now we use check constraint for thr age>18
 create table students2(
 student_id int primary key,
 age int check(age>18)
 );
 
 insert into students2 values
 (1,15),
 (2,19);
 
 
 
 insert into students2 values
 (1,20),
 (2,19);
 
 desc students2;
 
 create table result(
 student_id int primary key,
 student_marks int check(student_marks>350)
 );
 
 insert into result values
 (3,370),
 (4,400);
 
 select * from result;
 
 
 


 -- TOPIC: AUTO INCREMENT





 CREATE TABLE Doctor (
    d_id INT PRIMARY KEY,
    d_name VARCHAR(100) NOT NULL,
    d_performance VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) CHECK (salary > 50000) 
);


INSERT INTO Doctor (d_id, d_name, d_performance, salary) VALUES
(101, 'Dr. Amit Sharma', 'Excellent', 90000),
(102, 'Dr. Neha Verma', 'Very Good', 75000),
(103, 'Dr. Rahul Singh', 'Good', 60000),
(104, 'Dr. Priya Das', 'Outstanding', 120000),
(105, 'Dr. Vikram Rathore', 'Average', 55000),
(106, 'Dr. Anjali Mehta', 'Excellent', 95000),
(107, 'Dr. Suresh Raina', 'Good', 65000),
(108, 'Dr. Pooja Hegde', 'Very Good', 82000),
(109, 'Dr. Kabir Khan', 'Excellent', 110000),
(110, 'Dr. Simran Kaur', 'Good', 58000);


select * from doctor;


CREATE TABLE Patient (
    patient_id INT PRIMARY KEY,
    p_name VARCHAR(100) NOT NULL,
    d_id INT,
    FOREIGN KEY (d_id) REFERENCES Doctor(d_id)
);

INSERT INTO Patient (patient_id, p_name, d_id) VALUES
(201, 'Rohan Gupta', 101),
(202, 'Suman Rao', 102),
(203, 'Vikas Dubey', 101),
(204, 'Kavita Mishra', 103),
(205, 'Arjun Rampal', 104),
(206, 'Meera Chopra', 105),
(207, 'Titu Mama', 102),
(208, 'Sania Mirza', 108),
(209, 'Virat Kohli', 109),
(210, 'Deepika P', 110);

desc patient;

-- class 6
-- now we create doctor table and patient table 


--  Now we will use default onstraint

create table country(
countray_id int primary key,
country_name varchar(20) default "india"
);

insert into country (countray_id)
value
(1),(2);

select * from country;

-- now we use auto increment which is not a constraint it is an column atributes

create table students4(
student_id int primary key auto_increment,
student_name varchar(20) not null
);

desc students4;

insert into students4(student_name)
value
("aa"),
("bb");

select * from students4;

-- now we want the students_id to start from 100
create table students6(
student_id int primary key auto_increment,
student_name varchar(20) not null
)
auto_increment=100;

insert into students6(student_name)
value
("aa"),
("bb");


select * from students6;

