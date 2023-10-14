"""
19.	The length of the side of the cube is contained in the variable a. Write a 
program that calculates and displays the volume and surface area of the cube. Sample result:
Cube side: 4
Cube volume: 64
Cube surface area: 96
"""

a = int(input('Length of a side: '))
print('Volume:', a**3)
print('Surface area:', a**2 * 6)