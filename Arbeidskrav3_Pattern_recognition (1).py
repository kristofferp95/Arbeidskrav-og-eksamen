def isConsecutiveFour(values): 
    lst = values.split()
    count = 0
    for i in range(0, len(lst) -3):
        if lst[i] and lst[i + 1] and lst[i +2] and lst[i + 3] == lst[i]:
            count = 1
    
    if count == 1: 
        return f'The series has consecutives of fours'
    else:
        return f'The series has no consecutives of fours'
    

def main():
    values = input(f'Enter integers separated by spaces in one line: ')
    result = isConsecutiveFour(values)

    print(f'{result}')

main()
        
    