import math
circumference = float(input('Enter tree circumference: '))
radius = circumference/(2*math.pi)
diameter = 2*radius
print(f'Tree can be cut down: {diameter >= 50}')