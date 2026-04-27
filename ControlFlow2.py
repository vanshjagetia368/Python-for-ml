#In This we will learn about loops in python which includes for loops and while loops. We will also learn about nested loops and how to use them effectively in our code. Loops are a fundamental part of programming that allow us to execute a block of code multiple times based on a condition. They are essential for tasks such as iterating over data structures, performing repetitive tasks, and implementing algorithms. By mastering loops, we can write more efficient and concise code in Python.
#Starting with while loops, we will learn how to use them to execute a block of code as long as a specified condition is true. We will also explore the use of break and continue statements to control the flow of the loop. Next, we will move on to for loops, which are used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. We will learn how to use for loops with the range() function to create loops that execute a specific number of times. Finally, we will delve into nested loops, which are loops within loops, and see how they can be used to solve more complex problems. By the end of this chapter, you will have a solid understanding of how to use loops in Python effectively.
#While loops are used to execute a block of code repeatedly as long as a specified condition is true. The syntax for a while loop is as follows:
#while condition:
#    # code to be executed
#The condition is evaluated before the execution of the loop's body. If the condition is true, the code inside the loop is executed. After the code block is executed, the condition is evaluated again, and if it is still true, the loop continues to execute. This process repeats until the condition becomes false. It is important to ensure that the condition will eventually become false to avoid creating an infinite loop, which can cause the program to crash or become unresponsive. To prevent this, you can use a counter or modify the condition within the loop to ensure that it will eventually evaluate to false. Additionally, you can use the break statement to exit the loop prematurely if a certain condition is met, or the continue statement to skip the current iteration and move on to the next one.  
#Example 1: In this example, we will use a while loop to print the numbers from 1 to 10.
number = 1
while number <= 10:
    print(number)
    number += 1
#In this example, we initialize a variable number to 1. The while loop checks if number is less than or equal to 10. If the condition is true, it prints the current value of number and then increments number by 1. This process continues until number exceeds 10, at which point the loop terminates. The output of this code will be the numbers from 1 to 10, each printed on a new line.
#Example 2: In this example, we will use a while loop to create a simple guessing game where the user has to guess a number between 1 and 100.
import random
secret_number = random.randint(1, 100)
guess = None
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
#In this example, we generate a random secret number between 1 and 100 using the random module. We initialize the variable guess to None. The while loop continues to execute as long as guess is not equal to the secret number. Inside the loop, we prompt the user to input their guess and convert it to an integer. We then compare the guess to the secret number and provide feedback to the user. If the guess is too low, we print a message indicating that it is too low. If the guess is too high, we print a message indicating that it is too high. If the guess is correct, we print a congratulatory message and the loop terminates. This creates an interactive guessing game where the user can keep trying until they guess the correct number.
#Example 3: In this example, we will use a while loop to calculate the factorial of a given number.
number = int(input("Enter a number to calculate its factorial: "))
factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print("The factorial is:", factorial)
#In this example, we take input from the user for a number and initialize a variable factorial to 1. The while loop continues to execute as long as the number is greater than 1. Inside the loop, we multiply factorial by the current value of number and then decrement number by 1. This process continues until number is reduced to 1, at which point the loop terminates. Finally, we print the calculated factorial. For example, if the user inputs 5, the output will be "The factorial is: 120", since 5! = 5 * 4 * 3 * 2 * 1 = 120.
#Example 4: In this example, we will use a while loop to create a simple countdown timer that counts down from a specified number of seconds.
import time
seconds = int(input("Enter the number of seconds for the countdown: "))
while seconds > 0:
    print("Time remaining:", seconds, "seconds")
    time.sleep(1)  # Pause for 1 second
    seconds -= 1
print("Time's up!")
#In this example, we take input from the user for the number of seconds for the countdown and initialize the variable seconds with that value. The while loop continues to execute as long as seconds is greater than 0. Inside the loop, we print the remaining time and then use time.sleep(1) to pause the execution for 1 second. After the pause, we decrement seconds by 1. This process continues until seconds is reduced to 0, at which point the loop terminates and we print "Time's up!" to indicate that the countdown has finished. For example, if the user inputs 5, the output will be:
#Time remaining: 5 seconds
#Time remaining: 4 seconds
#Time remaining: 3 seconds
#Time remaining: 2 seconds
#Time remaining: 1 seconds
#Time's up!
#Example 5: In this example, we will use a while loop to create a simple menu-driven program that allows the user to perform different operations based on their choice.
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        print("Hello!")
    elif choice == '2':
        print("Goodbye!")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
#In this example, we use an infinite while loop (while True) to continuously display a menu to the user. The user is prompted to enter their choice, and based on the input, we use if, elif, and else statements to determine the appropriate response. If the user chooses '1', we print "Hello!". If they choose '2', we print "Goodbye!". If they choose '3', we print "Exiting the program." and use the break statement to exit the loop. If the user enters an invalid choice, we print a message asking them to try again. This creates a simple interactive menu-driven program that allows the user to perform different actions based on their input.    
#Now we will talk about for loops in Python. For loops are used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. The syntax for a for loop is as follows:
#for variable in iterable:
#    # code to be executed
#The variable takes on the value of each item in the iterable, one at a time, and the code block inside the loop is executed for each item. For loops are commonly used to iterate over a range of numbers using the range() function, which generates a sequence of numbers. The range() function can take one, two, or three arguments to specify the start, stop, and step of the sequence. For example, range(5) generates the numbers 0 to 4, while range(1, 6) generates the numbers 1 to 5, and range(0, 10, 2) generates the even numbers from 0 to 8. For loops can also be used to iterate over the elements of a list, tuple, or string directly, allowing you to perform operations on each element without needing to use an index. Additionally, you can use nested for loops to iterate over multi-dimensional data structures, such as lists of lists, to perform more complex operations. By mastering for loops, you can efficiently process and manipulate data in Python.
#Points to remember about for loops:
#1. For loops are used to iterate over a sequence or iterable object.
#2. The variable in the for loop takes on the value of each item in the iterable, one at a time.
#3. The code block inside the for loop is executed for each item in the iterable.
#4. The range() function can be used to generate a sequence of numbers for iteration.
#5. For loops can be used to iterate over lists, tuples, strings, and other iterable objects directly.
#6. Nested for loops can be used to iterate over multi-dimensional data structures.
#7.The step value cannot be zero in the range() function, as it would result in an infinite loop. If you try to use a step value of zero, Python will raise a ValueError indicating that the step argument must not be zero. Always ensure that the step value is a non-zero integer to avoid this error and to allow the for loop to function correctly.
#8.All three arguments (start, stop, step) in the range() function must be integers. If you try to use a non-integer value for any of these arguments, Python will raise a TypeError indicating that the arguments must be integers. Always ensure that you are using integer values for start, stop, and step when using the range() function to avoid this error and to allow the for loop to function correctly.

#Example 6: In this example, we will use a for loop to print the numbers from 1 to 10.
for number in range(1, 11):
    print(number)
#In this example, we use the range() function to generate a sequence of numbers from 1 to 10 (the stop value is exclusive, so we use 11). The for loop iterates over each number in the generated sequence, and the current number is printed in each iteration. The output of this code will be the numbers from 1 to 10, each printed on a new line.
#Example 7: In this example, we will use a for loop to iterate over a list of names and print a greeting for each name.
names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    print("Hello, " + name + "!")
#In this example, we have a list of names. The for loop iterates over each name in the list, and for each name, it prints a greeting message that includes the name. The output of this code will be:
#Hello, Alice!
#Hello, Bob!
#Hello, Charlie!
#Hello, David!
#Example 8: In this example, we will use the reversing concept in for loops to print the numbers from 10 to 1.
for number in range(10, 0, -1):
    print(number)
#In this example, we use the range() function with a step value of -1 to generate a sequence of numbers from 10 down to 1. The for loop iterates over each number in the generated sequence, and the current number is printed in each iteration. The output of this code will be the numbers from 10 to 1, each printed on a new line:
#Reverse a range using reversed function
for number in reversed(range(1, 11)):
    print(number)
#In this example, we use the reversed() function to reverse the sequence generated by range(1, 11). The for loop iterates over the reversed sequence, and the current number is printed in each iteration. The output of this code will also be the numbers from 10 to 1, each printed on a new line:
#Example 9: In this example, we will access the characters of a string using a for loop and print each character on a new line.
my_string = "Hello, World!"
for character in my_string:
    print(character)
#In this example, we have a string "Hello, World!". The for loop iterates over each character in the string, and for each character, it prints the character on a new line. The output of this code will be:
#Iterating a string in reverse order
for character in my_string[::-1]: #or you can also use reversed(my_string)
    print(character)
#In this example, we use the reversed() function to reverse the string "Hello, World!" and then iterate over the reversed string using a for loop. Each character is printed on a new line. The output of this code will be:
#!dlroW ,olleH
#Use of split function to iterate over words in a string
sentence = "This is a sample sentence."
for word in sentence.split():
    print(word) 
#In this example, we have a string "This is a sample sentence.". We use the split() method to split the string into a list of words. The for loop iterates over each word in the list, and for each word, it prints the word on a new line. The output of this code will be:
#This
#is
#a
#sample
#sentence.
#Iterating over a list of lists using nested for loops
matrix = [[1, 2, 3], [4, 5, 6 ], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element)
#In this example, we have a list of lists (a matrix). The outer for loop iterates over each row in the matrix, and the inner for loop iterates over each element in the current row. Each element is printed on a new line. The output of this code will be:
#1
#2
#3
#4
#5
#6
#7
#8
#9
#Another way to iterate over a list using for loop and enumerate function
fruits = ["apple", "banana", "cherry", "date"]
for i in fruits:
    print(i)
#In this example, we have a list of fruits. The for loop iterates over each fruit in the list, and for each fruit, it prints the fruit on a new line. The output of this code will be:
#apple
#banana
#cherry
#date
#Using enumerate function to get index and value while iterating over a list
for index, fruit in enumerate(fruits):
    print("Index:", index, "Fruit:", fruit)
#In this example, we use the enumerate() function to get both the index and the value while iterating over the list of fruits. The for loop iterates over the enumerated list, and for each fruit, it prints the index and the fruit on a new line. The output of this code will be:
#Index: 0 Fruit: apple
#Index: 1 Fruit: banana
#Index: 2 Fruit: cherry
#Index: 3 Fruit: date
#Accessing the values of a dictionary using for loop
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
for key in my_dict:
    print("Key:", key, "Value:", my_dict[key])
#In this example, we have a dictionary with keys "name", "age", and "city". The for loop iterates over each key in the dictionary, and for each key, it prints the key and its corresponding value on a new line. The output of this code will be:
#Key: name Value: Alice
#Key: age Value: 30
#Key: city Value: New York
#Accessing the items(Keys as well as values) of a dictionary using for loop
for i in my_dict.items():
    print(i)
#In this example, we use the items() method of the dictionary to get both the key and the value as a tuple while iterating over the dictionary. The for loop iterates over the items of the dictionary, and for each item (which is a tuple of key and value), it prints the item on a new line. The output of this code will be:
#('name', 'Alice')
#('age', 30)
#('city', 'New York')
#Accessing only the keys of a dictionary using for loop
for i in my_dict.keys():
    print(i)
#In this example, we use the keys() method of the dictionary to get only the keys while iterating over the dictionary. The for loop iterates over the keys of the dictionary, and for each key, it prints the key on a new line. The output of this code will be:
#name
#age
#city
#Accessing only the values of a dictionary using for loop
for i in my_dict.values():
    print(i)
#In this example, we use the values() method of the dictionary to get only the values while iterating over the dictionary. The for loop iterates over the values of the dictionary, and for each value, it prints the value on a new line. The output of this code will be:
#Alice
#30
#New York
#The use of if elif else statements and logical operators in for loops
for i in range(1, 11):
    if i % 2 == 0 and i % 3 == 0:
        print(i, "is divisible by both 2 and 3.")
    elif i % 2 == 0:
        print(i, "is divisible by 2.")
    elif i % 3 == 0:
        print(i, "is divisible by 3.")
    else:
        print(i, "is not divisible by either 2 or 3.")
#In this example, we use a for loop to iterate over the numbers from 1 to 10. Inside the loop, we use if, elif, and else statements along with logical operators to check if the current number is divisible by both 2 and 3, only by 2, only by 3, or neither. The appropriate message is printed based on the conditions that are true for each number in the range. The output of this code will be:
#1 is not divisible by either 2 or 3.
#2 is divisible by 2.
#3 is divisible by 3.
#4 is divisible by 2.
#5 is not divisible by either 2 or 3.
#6 is divisible by both 2 and 3.
#7 is not divisible by either 2 or 3.
#8 is divisible by 2.
#9 is divisible by 3.
#10 is divisible by 2.
#The use of break and continue statements in for loops
for i in range(1, 11):
    if i == 5:
        print("Breaking the loop at", i)
        break
    elif i == 3:
        print("Skipping the number", i)
        continue
    print(i)
#In this example, we use a for loop to iterate over the numbers from 1 to 10. Inside the loop, we check if the current number is equal to 5. If it is, we print a message and use the break statement to exit the loop. If the current number is equal to 3, we print a message and use the continue statement to skip the rest of the loop for that iteration and move on to the next number. For all other numbers, we simply print the number. The output of this code will be:
#1
#2
#Skipping the number 3
#4
#Breaking the loop at 5     
#6, 7, 8, 9, and 10 will not be printed because the loop is broken at 5.
#The break statement is used to exit a loop prematurely when a certain condition is met, while the continue statement is used to skip the current iteration of the loop and move on to the next iteration. In this example, we will use both break and continue statements in a for loop to demonstrate their functionality.
#The Continue statement is used to skip the current iteration of the loop and move on to the next iteration. In this example, we will use the continue statement to skip printing the number 3 in the loop.
#Nested for loops are for loops inside another for loop. They are used to iterate over multi-dimensional data structures, such as lists of lists, to perform more complex operations. The syntax for nested for loops is as follows:
#for variable1 in iterable1:
#    for variable2 in iterable2:
#        # code to be executed
#In this structure, the outer loop iterates over iterable1, and for each iteration of the outer loop, the inner loop iterates over iterable2. This allows you to access and manipulate elements in a multi-dimensional data structure. Nested for loops can be used for tasks such as iterating over a matrix, creating patterns, or performing operations on combinations of elements from two or more iterables. It is important to be mindful of the complexity of nested loops, as they can lead to increased time complexity if not used efficiently. Always consider the size of the data and the number of iterations when using nested loops to ensure that your code runs efficiently.
#Example of nested for loops: In this example, we will use nested for loops to print a multiplication table from 1 to 5.
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()  # Print a new line after each row
#In this example, we have an outer for loop that iterates over the numbers from 1 to 5 (inclusive) using range(1, 6). Inside the outer loop, we have an inner for loop that also iterates over the numbers from 1 to 5. The inner loop calculates the product of i and j and prints it, with end="\t" to separate the values with a tab. After the inner loop completes for each value of i, we print a new line to move to the next row of the multiplication table. The output of this code will be:
#1	2	3	4	5
#2	4	6	8	10
#3	6	9	12	15
#4	8	12	16	20
#5	10	15	20	25 
#Nested while loops are while loops inside another while loop. They are used to perform more complex operations that require multiple levels of iteration. The syntax for nested while loops is as follows:
#while condition1:
#    while condition2:
#        # code to be executed
#In this structure, the outer while loop continues to execute as long as condition1 is true, and for each iteration of the outer loop, the inner while loop continues to execute as long as condition2 is true. This allows you to perform operations that require multiple levels of iteration, such as iterating over a multi-dimensional data structure or implementing a more complex algorithm. It is important to ensure that the conditions for both the outer and inner loops will eventually become false to avoid creating infinite loops. Always consider the logic of your nested while loops to ensure that they function correctly and efficiently.
#Example of nested while loops: In this example, we will use nested while loops to print a pattern of asterisks.
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()  # Print a new line after each row
    i += 1
#In this example, we have an outer while loop that iterates from 1 to the number of rows (5 in this case). Inside the outer loop, we have an inner while loop that iterates from 1 to the current value of i. The inner loop prints an asterisk for each iteration, with end="" to keep the asterisks on the same line. After the inner loop completes for each value of i, we print a new line to move to the next row of the pattern. The output of this code will be:
#*
#**
#***
#****
#***** 
#Comibining if statements and loops: In this example, we will use if statements inside a for loop to determine if the numbers from 1 to 10 are even or odd.
for number in range(1, 11):
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")
#In this example, we use a for loop to iterate over the numbers from 1 to 10. Inside the loop, we use an if statement to check if the current number is even (i.e., divisible by 2 with no remainder). If the condition is true, we print a message indicating that the number is even. If the condition is false, we use the else statement to print a message indicating that the number is odd. The output of this code will be:
#1 is odd.
#2 is even.
#3 is odd.
#4 is even.
#5 is odd.
#6 is even.
#7 is odd.
#8 is even.
#9 is odd.
#10 is even.   
#Now we will go on some examples of while and for loops combined with if statements and logical operators to create more complex programs. These examples will demonstrate how to use control flow statements effectively in combination with loops to solve real-world problems and make decisions based on user input or data processing. We will explore various scenarios where we can apply these concepts to create interactive and dynamic programs that can handle different conditions and provide meaningful output based on the logic implemented within the loops and if statements. By working through these examples, you will gain a deeper understanding of how to use control flow statements in conjunction with loops to create more sophisticated and functional Python programs.   
# Example 1: Even and Odd Counter
print("\nExample 1: Even and Odd Counter")
even = 0
odd = 0
for i in range(1, 21):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)

# Output:
# Even: 10 Odd: 10


# Example 2: Sum of Multiples of 3
print("\nExample 2: Sum of Multiples of 3")
i = 1
total = 0
while i <= 30:
    if i % 3 == 0:
        total += i
    i += 1
print("Sum:", total)

# Output:
# Sum: 165


# Example 3: Character Counter
print("\nExample 3: Character Counter")
text = "abc123"
letters = digits = 0
for ch in text:
    if ch.isdigit():
        digits += 1
    else:
        letters += 1
print("Letters:", letters, "Digits:", digits)

# Output:
# Letters: 3 Digits: 3


# Example 4: Number Classifier
print("\nExample 4: Number Classifier")
i = 1
while i <= 5:
    if i < 3:
        print(i, "Low")
    elif i < 5:
        print(i, "Medium")
    else:
        print(i, "High")
    i += 1

# Output:
# 1 Low
# 2 Low
# 3 Medium
# 4 Medium
# 5 High


# Example 5: Divisibility Check
print("\nExample 5: Divisibility Check")
for i in range(1, 11):
    if i % 2 == 0 and i % 5 == 0:
        print(i, "Both")
    elif i % 2 == 0:
        print(i, "Even")
    elif i % 5 == 0:
        print(i, "Five")
    else:
        print(i, "None")

# Output:
# 1 None
# 2 Even
# 3 None
# 4 Even
# 5 Five
# 6 Even
# 7 None
# 8 Even
# 9 None
# 10 Both


# -------- ADVANCED EXAMPLES --------


# Example 6: Student Performance Analyzer
print("\nExample 6: Student Performance")
students = [("A", 85), ("B", 45), ("C", 72)]

for name, marks in students:
    if marks >= 80:
        if marks >= 90:
            print(name, "Excellent")
        else:
            print(name, "Very Good")
    elif marks >= 50:
        if marks >= 70:
            print(name, "Good")
        else:
            print(name, "Average")
    else:
        if marks < 35:
            print(name, "Fail")
        else:
            print(name, "Needs Improvement")

# Output:
# A Very Good
# B Needs Improvement
# C Good


# Example 7: Transaction Processing
print("\nExample 7: Transaction Processing")
transactions = [500, 2000, 15000]

for amount in transactions:
    if amount > 10000:
        if amount > 20000:
            print(amount, "High")
        else:
            print(amount, "Medium High")
    elif amount > 1000:
        if amount % 2 == 0:
            print(amount, "Standard")
        else:
            print(amount, "Odd Check")
    else:
        print(amount, "Low")

# Output:
# 500 Low
# 2000 Standard
# 15000 Medium High


# Example 8: Login Attempt System
print("\nExample 8: Login System")
correct = "admin"
attempts = 2

while attempts > 0:
    user = "wrong"
    if user == correct:
        print("Access Granted")
        break
    else:
        if attempts == 1:
            print("Last attempt")
        else:
            print("Invalid")
    attempts -= 1

if attempts == 0:
    print("Blocked")

# Output:
# Invalid
# Last attempt
# Blocked


# Example 9: Data Filtering
print("\nExample 9: Data Filtering")
data = [12, 67, 23]

for num in data:
    if num > 50:
        if num % 2 == 0:
            print(num, "Large Even")
        else:
            print(num, "Large Odd")
    else:
        if num < 20:
            print(num, "Small")
        else:
            print(num, "Medium")

# Output:
# 12 Small
# 67 Large Odd
# 23 Medium


# Example 10: Inventory Monitoring
print("\nExample 10: Inventory")
items = {"A": 50, "B": 5, "C": 0}

for item, qty in items.items():
    if qty == 0:
        print(item, "Out")
    elif qty < 10:
        if qty < 5:
            print(item, "Critical")
        else:
            print(item, "Low")
    else:
        if qty > 40:
            print(item, "Overstock")
        else:
            print(item, "OK")

# Output:
# A Overstock
# B Low
# C Out


# Example 11: Pattern Decision
print("\nExample 11: Pattern")
rows = 3

for i in range(1, rows + 1):
    if i % 2 == 0:
        for j in range(i):
            print("#", end="")
    else:
        for j in range(i):
            print("*", end="")
    print()

# Output:
# *
# ##
# ***


# Example 12: Multi Condition System
print("\nExample 12: Multi Condition")
numbers = [10, 25, 40]

for n in numbers:
    if n % 5 == 0:
        if n % 2 == 0:
            if n > 20:
                print(n, "Even >20")
            else:
                print(n, "Even <=20")
        else:
            if n > 20:
                print(n, "Odd >20")
            else:
                print(n, "Odd <=20")
    else:
        print(n, "No")

# Output:
# 10 Even <=20
# 25 Odd >20
# 40 Even >20