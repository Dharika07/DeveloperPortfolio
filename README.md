# DeveloperPortfolio

## Beginner Developer Ecosystem Portfolio

Welcome to my Developer Portfolio! This repository showcases the technical skills, practical knowledge and learning progress I gained throughout my semester.

**Student Details**
- Name: Dharika
- Course: B.Tech CSE (AI & ML)
- University: K.R. Mangalam University
- Project: Semester Capstone Project

## Project Objectives

The main objective of this project is to demonstrate practical knowledge of Linux commands, Shell Scripting, API Integration using Python and professional portfolio development.

## Repository Structure

| Folder | Description |
|---|---|
| Linux | Linux commands and system profile |
| ShellScripts | Bash automation scripts |
| API | API response JSON and Python scripts |
| Portfolio | Resume, LinkedIn profile and learning roadmap |
| Screenshots | Supporting screenshots of all labs |

## Skills Learned

- Linux Command Line
- Bash Shell Scripting
- Python Programming
- API Integration
- JSON Data Handling
- Git and GitHub
- Professional Portfolio Development
- Technical Documentation

## Tools and Technologies

- Ubuntu Linux
- Bash
- Python
- Git
- GitHub
- Markdown

## Learning Outcomes

Through this project, I aim to improve my programming, problem-solving, automation and documentation skills.

## Conclusion

This repository represents my semester learning journey and practical implementation of the concepts covered in all four laboratory sections.

**Created by Dharika**


# Bash Automation Scripts

## Objective
To learn shell scripting and automate basic tasks using Bash in Ubuntu Linux.

## Program 1: Print Numbers from 1 to 10

### Description
This program uses a for loop to print numbers from 1 to 10.

### Concepts Used
- Bash Scripting
- For Loop
- Variables
- Echo Command

### Code
```bash
#!/bin/bash

for i in {1..10}
do
    echo $i
done
```

### Output
```text
1
2
3
4
5
6
7
8
9
10
```

## Program 2: Check Odd or Even Number

### Description
This program takes a number from the user and checks whether it is odd or even using if-else conditions.

### Concepts Used
- User Input
- Read Command
- Modulus Operator
- If-Else Condition

### Code
```bash
#!/bin/bash

echo "Enter a number:"
read num

if [ $((num % 2)) -eq 0 ]
then
    echo "$num is an Even number"
else
    echo "$num is an Odd number"
fi
```

### Sample Output
```text
Enter a number:
8
8 is an Even number
```

## Conclusion
These Bash programs demonstrate the use of loops, variables, user input and conditional statements in Linux shell scripting.

