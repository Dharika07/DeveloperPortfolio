
# Bash Automation Scripts

## Objective
To learn shell scripting and automate basic tasks using Bash.

## Scripts Included
1. Print numbers from 1 to 10 using a loop.
2. Identify odd and even numbers using if-else.
3. Perform basic mathematical operations.
4. Display system date and username.

## Concepts Used
- Variables
- Loops
- If-Else Conditions
- Input and Output
- Bash Commands

## Conclusion
Shell scripting helps automate repetitive tasks in Linux.


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
