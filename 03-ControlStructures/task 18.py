"""
18.	A variable x has a value of 7 and a variable y has a value of 34. Write a program that swaps variable 
values (x should be 34 and y should be 7). You can use one additional, auxiliary variable. Sample result:
Value of x: 7
Value of y: 34
Value of x after swapping: 34
Value of y after swapping: 7
"""

x = 7
x1 = 7
y = 34
print (f'x is {x} and y is {y}')
x = y
y = x1
print(f'now x is {x} and y is {y}')