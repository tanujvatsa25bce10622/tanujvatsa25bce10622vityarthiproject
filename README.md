Student Record Management System

Introduction
This is a very basic, menu-driven Python program to manage student information in a college or school setting. It is designed for first-year students and uses only Python basics like lists, dictionaries, input/output, loops, and type conversion. The project does not use files or databases; all information is stored in memory while the program runs.

What This Program Does
The program acts as a digital replacement for manual record-keeping. Users can:

Add student details (roll number, name, branch)

View the list of all students

Add and view marks/grades for each student (for any subject)

Mark and check attendance for any student

Repeat these actions as many times as desired using a menu

How Marks are Counted
When you select "Add Marks," you enter a roll number, subject, and marks (numerical value).

The marks are stored in a dictionary under the student’s roll number and subject.

Each student can have marks for multiple subjects, all stored separately.

When you choose "Show Marks," the program lists all marks recorded for that student.

How To Run
Make sure Python (version 3 or above) is installed on your computer.

Download or copy the code file, e.g. student_record_system.py.

Open the terminal (command prompt) and browse to the location of your file.

Run the command:

text
python student_record_system.py
The program will show a menu in the terminal. Enter the number for any option you wish to use.

Files in This Project
student_record_system.py – main and only code file with all logic and menu
README.md – this documentation file for easy understanding
assets – folder for screenshots or diagrams, e.g. of the running program or workflow
