s = input(f'Enter integers of your choice separated by one space: ')
list1 = list(map(int, s.split()))
list2 = []
count = 0 

while count < len(list1): 
    if list1[count] not in list2:
        list2.append(list1[count])
        count += 1
    else:
        count += 1
    
print(f'The number of distinct number is {len(list2)}')
print(f'The distinct numbers are {" ".join(str(x) for x in list2)}')

