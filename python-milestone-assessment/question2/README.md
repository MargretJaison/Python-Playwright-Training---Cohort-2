# Question 2 - Simple Employee File Management
 
# Problem Statement

You are working on a small Python application that maintains employee information. Employee details need to be stored in a file and later read to generate a simple report.

Requirements

1. Create a file called employees.txt.
2. Store employee details such as: Employee ID, Name, Role, and Salary.
3. Read the employee information from the file.
4.	Display all employees.
5.	Find and display employees whose salary is greater than ₹50,000.
6.	Find the employee with the highest salary.
7.	Count how many employees belong to each role.
8.	Use functions such as add_employee(), read_employees(), find_highest_salary(), and find_employees_by_role().
9.	Use a context manager (with open()) while working with the file.
10.	Handle the situation where the file does not exist using exception handling.
11.	Create a simple Employee class with employee_id, name, role, and salary.
12.	Create a method such as display_details().

 
# Approach / Logic
1. Create an Employee class with a constructor and display_details() method.
2. Store employee records in employees.txt.
3. Use add_employee() to append new employee records.
4. Use read_employees() to read the file.
5. Handle FileNotFoundError using exception handling.
6. Use find_highest_salary() to identify the highest-paid employee.
7. Use find_employees_by_role() to count employees by role.
8. Use with open() as a context manager.
 
# How to Run
1. Keep main.py and employees.txt in the question2 folder.
2. Open a terminal in that folder.
3. Run: python main.py
 
# Sample Input
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000
 
# Sample Output
===== Employee Details =====
 
101 - Rahul - Python Developer - ₹50000
102 - Anjali - Tester - ₹45000
103 - John - Developer - ₹60000
104 - Priya - Tester - ₹48000
 
===== Employees with Salary > 50000 =====
 
John - ₹60000
 
Highest Paid Employee:
John - ₹60000
 
Employee Count by Role:
Developer: 1
Python Developer: 1
Tester: 2
 
# Python Concepts Used
- Classes and objects
- Constructor and methods
- File handling
- Context managers
- Exception handling
- Functions
- Lists and dictionaries
- Loops and conditions