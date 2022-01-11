def isSorted(lst):
    list1 = lst.split()
    list2 = list1.copy()
    list1.sort()

    if list1 == list2: 
        answer = f'The list is sorted'
    else: 
        answer = f'The list is not sorted'
    
    return answer 

def main():
    lst = input(f'Enter numbers with in one line and with one space between them: ')
    result = isSorted(lst)

    print(f'{result}')

main()




    
