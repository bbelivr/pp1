height = int(input('Your height: '))
feet = height * 0.032808399
print(f'{int(feet//1)} feet and {round(feet%1 * 10)} inches')