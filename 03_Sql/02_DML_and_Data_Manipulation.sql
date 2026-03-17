-- ---------------------------------------------------------
-- MODULE 02: DML OPERATIONS (INSERT, UPDATE, DELETE)
-- 👤 AUTHOR: Maaz Usmani
-- ---------------------------------------------------------





/*******************************************************************************
        📊 DATA MANIPULATION LANGUAGE (DML) & QUERY OPERATIONS 📊
*******************************************************************************
    
    Author: Maaz Usmani
    Topic: SQL DML (INSERT, UPDATE, DELETE) & DQL (SELECT)
    Purpose: Learning Database Record Management
    Date: March 2026
    
*******************************************************************************/

-- 1. INSERT COMMAND (Adding New Records)
-- Naya data table mein dalne ke liye use hota hai.
INSERT INTO Students (id, name, age, course) 
VALUES (101, 'Maaz Usmani', 21, 'Full Stack Development');


-- 2. SELECT COMMAND / DQL (Fetching Records)
-- Data ko dekhne aur filter karne ke liye.
SELECT * FROM Students;
SELECT name, course FROM Students WHERE id = 101;


-- 3. UPDATE COMMAND (Modifying Existing Records)
-- Purane data ko update ya change karne ke liye.
UPDATE Students 
SET course = 'Django & React Framework' 
WHERE id = 101;


-- 4. DELETE COMMAND (Removing Records)
-- Table se specific records ko delete karne ke liye.
DELETE FROM Students 
WHERE id = 101;

/*******************************************************************************
                           END OF DML OPERATIONS
*******************************************************************************/








-- JUSTP PRACTICE FROM DIFFRENT TABLE







create table employee_6(id int primary key,name varchar(20),city varchar(20));
alter table employee_6 add email varchar(50);
alter table employee_6 add (salary int, phone_no varchar(20));
alter table employee_6 modify salary int;
desc employee_6;
insert into employee_6 values(1,"maaz","bhopal","maazusmani15@gmail.com",50000,"7324886683");
select * from employee_6;
alter table employee_6 rename column name to first_name;
alter table employee_6 rename column email to my_email;
alter table employee_6 rename to employee_data;
-- update 
set sql_safe_updates=0;
update employee_data set salary=20000;
insert into employee_data values(2,"maaz","delhi","fahausmani15@gmail.com",100000,"9224886683");
insert into employee_data values(3,"amjad","mumbai","shibliusmani15@gmail.com",200000,"3654886683");
update employee_data set city="bhopal" where id=2;
select * from employee_data;
update employee_data set first_name="sahil" where id=3;
alter table employee_data drop column phone_no;
select * from employee_data;
delete from employee_data where id=1;






