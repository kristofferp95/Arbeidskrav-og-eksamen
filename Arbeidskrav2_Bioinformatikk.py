s = str(input(f'Enter a Genome string: '))
start = -1
gene = 0

for i in range(0, len(s)):
    outPutString = s[i : i + 3]
    if outPutString == "ATG": 
        start = i + 3
    elif outPutString == "TAG" or outPutString == "TAA" or outPutString == "TGA" and start != -1:
        genome = s[start : i]

        if len(genome) % 3 == 0:
            print(f'{genome}')
            start = -1
            gene = 1

if gene == 0: 
    print(f'no gene is found')







    
    





