price = float(input('Price: '))
discount = float(input('Discount: '))
print(f'Price with discount: {round(price - price*discount/100, 2)}')
print(f'Reduction: {round(price*discount/100, 2)}')