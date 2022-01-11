def reverse1(number):
    reverseNumber = 0
    while number > 0: 
        remainder = number % 10
        reverseNumber = (reverseNumber * 10) + remainder
        number = number // 10
        
    return reverseNumber

def isPalindrome(number):
    if number == reverse1(number):
        answer = str(f'{number} is a palindrome')
    else: 
        answer = str(f'{number} is not a palindrome')
        
    return answer

def main():
        value = int(input(f'Enter a random integer: '))
        result = isPalindrome(value)
        print(f'{result}')
main()