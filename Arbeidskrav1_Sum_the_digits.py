value = int(input(f'Enter a value between 0 and 1000: '))

digit1 = value // 1000
newValue = value % 1000 
digit2 = newValue // 100 
newValue = newValue % 100 
digit3 = newValue // 10
newValue = newValue % 10 
digit4 = newValue // 1

sum = digit1 + digit2 + digit3 + digit4

print(f'The sum of the integer is {sum}')

