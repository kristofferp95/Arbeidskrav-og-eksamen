def format(seconds):
    hours = (seconds // 3600) % 24
    minutes = (seconds // 60) % 60
    seconds1 = seconds % 60

    return (f'{hours:0>2}:{minutes:0>2}:{seconds1:0>2}')


def main(): 
    input1 = int(input(f'Enter number of seconds: '))
    result = format(input1)

    print(f'The number of hours, minutes and seconds for total seconds {input1} is {result}')

main()
