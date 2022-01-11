
number = int(input(f'Enter a value between 0 and 15: '))
list1 = []

while number > 0: 
    result = number % 2
    list1.append(result)
    number = number // 2

list1.reverse()
for i in range(0, len(list1)):
    print(f'{list1[i]}', end = '')

    