#Now we will learn about control flow in python which incudes if statements, loops
#Control flow refers to the order in which individual statements, instructions, or function calls are executed or evaluated in a programming language. In Python, control flow is managed using various constructs such as if statements, loops, and functions.
#1. If Statements:
#If statements are used to execute a block of code only if a specified condition is true.
#Syntax:
# if condition:
#     # block of code to be executed if the condition is true
#Example:
x = 10
if x > 5:
    print("x is greater than 5")
#Output: x is greater than 5
#In this example, the condition x > 5 is true, so the block of code inside the if statement is executed, and "x is greater than 5" is printed.
#else statements can be used to execute a block of code if the condition is false.
#Syntax:
# if condition:
#     # block of code to be executed if the condition is true
# else:
#     # block of code to be executed if the condition is false
#Example:
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
#Output: x is not greater than 5
#In this example, the condition x > 5 is false, so the block of code
#inside the else statement is executed, and "x is not greater than 5" is printed.
#else if statements can be used to check multiple conditions.
#Syntax:
# if condition1:
#     # block of code to be executed if condition1 is true
# elif condition2:
#     # block of code to be executed if condition2 is true
# else:
#     # block of code to be executed if both condition1 and condition2 are false
#Example:
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but not greater than 10")
else:
    print("x is not greater than 5")
#Output: x is greater than 5 but not greater than 10
#In this example, the condition x > 10 is false, but the condition x > 5 is true, so the block of code inside the elif statement is executed, and "x is greater than 5 but not greater than 10" is printed. 
#Nested if statements can be used to check multiple conditions within another condition.
#Syntax:
# if condition1:
#     if condition2:
#         # block of code to be executed if both condition1 and condition2 are true
#     else:
#         # block of code to be executed if condition1 is true but condition2 is false
# else:
#     # block of code to be executed if condition1 is false
#Example:
x = 8
if x > 5:
    if x < 10:
        print("x is greater than 5 and less than 10")
    else:
        print("x is greater than or equal to 10")
else:
    print("x is not greater than 5")
#Output: x is greater than 5 and less than 10
#In this example, the condition x > 5 is true, so we check the next condition x < 10, which is also true. Therefore, the block of code inside the nested if statement is executed, and "x is greater than 5 and less than 10" is printed.   
