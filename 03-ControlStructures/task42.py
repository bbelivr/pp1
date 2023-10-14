number = input('Enter binary number: ')
decimal = int(number[0])*2**3 + int(number[1])*2**2 + int(number[2])*2**1 + int(number[3])*2**0
print(f'Binary number in decimal notation: {decimal}')