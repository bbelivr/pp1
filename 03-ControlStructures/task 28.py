height = int(input('Enter your height in cm: '))
weight = int(input('Enter your weight in kg: '))
height /= 100
print('Your BMI:', round(weight/height**2, 2))
print('Correct weight:', 24.9 >= round(weight/height**2, 2) >= 18.5 )