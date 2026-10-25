 
# Question 1 - Student Marks Management System
 
# Problem Statement

You are asked to develop a simple Python program to manage student marks. The program should accept details of multiple students, calculate their results, and display a summary.

# Requirements

1.	Store the following information for each student: Student ID, Student Name, Python Marks, SQL Marks, and AI Marks.
2.	Calculate Total Marks, Average Marks, and Grade.
3.	Display whether the student is PASS (average >= 40) or FAIL (average < 40).
4.	Display the student who has the highest average.
5.	Display the list of students who scored more than 75 average marks.
6.	Use appropriate Lists, Dictionaries, Functions, Conditional Statements, and Loops.
7.	Use at least one List Comprehension.
8.	Display the final result in a readable format.

 
# Approach / Logic
1. Store student details in dictionaries.
2. Store multiple students in a list.
3. Use functions to calculate grades, results, and display details.
4. Use conditional statements to determine grades and pass/fail status.
5. Use a loop to accept and display student details.
6. Use max() to find the student with the highest average.
7. Use list comprehension to find students scoring above 75.
 
# How to Run
1. Open a terminal in the question1 folder.
2. Run: python main.py
 
# Sample Input
Number of students: 2
 
Student 1:
ID: 101
Name: Rahul
Python: 80
SQL: 75
AI: 85
 
Student 2:
ID: 102
Name: Anjali
Python: 65
SQL: 60
AI: 70
 
# Sample Output
===== Student Result =====
 
Student ID: 101
Name: Rahul
Total: 240
Average: 80
Grade: A
Result: PASS
 
Student ID: 102
Name: Anjali
Total: 195
Average: 65
Grade: B
Result: PASS
 
Highest Scoring Student: Rahul
Students above 75: Rahul
 
# Python Concepts Used
- Lists and dictionaries
- Functions
- Loops and conditional statements
- Arithmetic calculations
- List comprehension
- String formatting