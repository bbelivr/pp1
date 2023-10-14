employee = 'Mr. John May, born on 1998-02-16'
name = employee[3:8]
surname = employee[8:12]
print('Description:', employee)
print('Name:', name)
print('Surname:', surname)
initials = employee[4] + employee[9]
print('Initials:', initials)
born = employee[21:]
print('Born:', born)