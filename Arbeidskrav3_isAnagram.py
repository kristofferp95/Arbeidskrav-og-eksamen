def isAnagram(s1, s2): 
    list1 = list(s1)
    list2 = list(s2)
    count = 0

    for i in range(0, len(list1)):
        if list1[i] in list2: 
            count += 1
        else:
            count = 0
    
    if count == len(list1): 
        answer = f'{s1} and {s2} are anagram'
    else: 
        answer = f'{s1} and {s2} are not anagram'

    return answer

def main(): 
    s1 = input(f'Enter a word: ')
    s2 = input(f'Enter a word: ')
    result = isAnagram(s1, s2)

    print(f'{result}')

main()
    


