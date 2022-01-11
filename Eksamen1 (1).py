def isPrime(n): 
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True

def isPrimeReversed(n):
    n = str(n)
    lst = list(n)
    lst.reverse()
    lst = int(''.join(lst))
    if lst > 1:
        for i in range(2, int(lst/2)+1):
            if (lst % i) == 0:
                return False
        else:
            return True

def main():
    list = []
    count = 0
    number = 2

    while count < 20:
        if isPrime(number) == True and isPrimeReversed(number) == True:
            list.append(number)
            count += 1
            number +=1
        else: 
            number +=1
    
    for i in range(0, 20, 5):
        for j in range(i, i+5):
            print(f'{list[j]}', end = ' ')
        print()
main()