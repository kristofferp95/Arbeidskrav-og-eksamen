import random
def rollDices(): 
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    totalSum = dice1 + dice2
    return totalSum


def main(): 
    lst = []
    for i in range(0, 1000):
        number = rollDices()
        lst.append(number)
    
    print(f'Total - simulated  - expected')
    print(f'{"":7} {"Percent":10} {"percent":<12} ')
    down = 3
    for i in range(2, 13):
        amount = lst.count(i)
        simulated = (amount * 100) / 1000
        if i <= 7:
            expected = (i - 1)*100 / 36
        else: 
            expected = (i - down)*100 / 36 
            down += 2
        print(f'{i:<7} {simulated:<10.2f} {expected:<12.2f}')

        

main()