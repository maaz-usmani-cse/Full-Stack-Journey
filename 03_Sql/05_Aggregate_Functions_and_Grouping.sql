/*******************************************************************************
    📂 FILE: 05_Aggregate_Functions_and_Grouping.sql
    👤 AUTHOR: Maaz Usmani
    🎯 TOPIC: SQL Aggregate Functions & Data Grouping
   
*******************************************************************************
    In this file, we explore how to perform calculations on multiple rows 
    and group the data based on specific columns.
*******************************************************************************/

-- 1. COUNT() : Total number of records count karne ke liye
-- Example: Total students kitne hain?
SELECT COUNT(*) AS Total_Students FROM Students;


-- 2. SUM() : Numeric columns ka total nikalne ke liye
-- Example: Saare students ki total fees kitni jama hui?
SELECT SUM(fees_paid) AS Total_Revenue FROM Students;


-- 3. AVG() : Average value nikalne ke liye
-- Example: Students ki average age kya hai?
SELECT AVG(age) AS Average_Age FROM Students;


-- 4. MIN() & MAX() : Lowest aur Highest value nikalne ke liye
-- Example: Sabse kam aur sabse zyada fees kisne di?
SELECT MIN(fees_paid) AS Minimum_Fee, MAX(fees_paid) AS Maximum_Fee FROM Students;


-- 5. GROUP BY : Data ko categories mein baantne ke liye
-- Example: Har course mein kitne students hain?
SELECT course, COUNT(id) AS Student_Count
FROM Students
GROUP BY course;


-- 6. HAVING CLAUSE : Grouped data par filter lagane ke liye
-- Example: Wo courses dikhao jisme 5 se zyada students hain?
SELECT course, COUNT(id) AS Student_Count
FROM Students
GROUP BY course
HAVING COUNT(id) > 5;




--7. Kitne alag-alag (unique) courses mein admissions hue hain?
SELECT COUNT(DISTINCT course) AS Unique_Courses_Count FROM Students;




-- 8.-- Average age ko 2 decimal places tak round karna
SELECT ROUND(AVG(age), 2) AS Clean_Average_Age FROM Students;





-- 9.-- Har city mein, har course ke kitne students hain?
SELECT city, course, COUNT(*) AS Student_Count
FROM Students
GROUP BY city, course;



/*******************************************************************************
                 🔥 SQL TIP: Always use 'AS' for Aliases! 
       It makes your output column names much cleaner and readable.
*******************************************************************************/