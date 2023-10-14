number = input('Credit card number: ')
number1 = number[:4] + ' ' + number[4:8] + ' ' + number[8:12] + ' ' + number[12:]
print(f'Credit card number: {number1}')