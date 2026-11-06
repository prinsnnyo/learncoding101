# Problem: Check if a Number is Even or Odd

# Description: Write a Python program that asks the user to enter an integer. The program should determine whether the number is even or odd and display the result.

# Solution:
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")