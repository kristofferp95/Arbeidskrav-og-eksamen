def locateLargest(a):
    biggest = 0
    for i in range(0, len(a)): 
        for j in range(0, len(a[0])):
            check = float(a[i][j])
            if check > biggest:
                biggest = check
                result = f'The location of the largest element is at {i, j}'
    return result


def main():
    rows = int(input(f'Enter the number of rows in the list: '))
    numbers = []
    for i in range(0, rows): 
        lst1 = input(f'Enter a row: ')
        numbers.append(lst1.split())
    
    result = locateLargest(numbers)
    print(result)

main()



