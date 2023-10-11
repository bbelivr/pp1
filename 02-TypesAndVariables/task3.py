father = int(input('Enter father’s income: '))
mother = int(input('Enter mother’s income: '))
number = int(input('Enter number of people in family: '))
total = father + mother
person = total / number
print(f'Income per person: {person}')