def get_login_name(firstName, lastName, id):
    firstName = list(firstName)
    if len(firstName) <= 3:
        firstName = firstName
    else:
        firstName = firstName[0:3]
    firstName = ''.join(firstName)

    lastName = list(lastName)
    if len(lastName) <= 3:
        lastName = lastName
    else:
        lastName = lastName[0:3]
    lastName = ''.join(lastName)

    id = list(id)
    if len(id) <= 3: 
        id = id 
    else:
        id = id[len(id)-3:]
    id = ''.join(id)


    print(f'your id number is: {firstName}{lastName}{id}')


def main():
    firstName = input(f'Enter your first name: ')
    lastName = input(f'Enter your last name: ')
    id = (input(f'Enter your student Id number: '))

    get_login_name(firstName, lastName, id)
main()