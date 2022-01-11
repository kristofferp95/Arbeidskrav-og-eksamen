def valid_password(password):
    password = list(password)
    newpassord = []
    print(newpassord)
    for i in range(0, len(password)):
        newpassord.append(ord(password[i]))
    print(newpassord)

    small = 0
    big = 0
    number = 0

     
    for i in range(65, 91):
            if newpassord.count(i) > 0:
                big = 1

    for i in range(97, 123):
            if newpassord.count(i) > 0:
                small = 1
        
    for i in range(48, 58):
            if newpassord.count(i) > 0:
                number = 1

    
    if number == 1 and small == 1 and big == 1 and len(newpassord) >=7:
        return True
    else:
        return False
    


def main():
    k = input("enter your password: ")
    c = valid_password(k)
    if c == True:
        print("valid password")
    else:
        print("Not a valid password")


main()
        



    


    