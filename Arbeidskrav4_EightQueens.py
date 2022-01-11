
class EQ: 
    def __init__(self, queens = 8 * [-1]):
        self.queens = queens

    def get(self, i):
        return self.queens[i]

    def set(self, i, j):
        self.queens.insert(i, j)

    def isSolved(self):
        sum = 0
        for i in range(0, len(self.queens)):
            k = self.queens.count(i)
            if k > 1: 
                sum = 1
                return f'No'   
        
        if sum == 0: 
            sum2 = 0
            z = 8
            for i in range(0, 7):
                z -= 1
                for j in range(1, z):
                    if self.queens[i + j] == self.queens[i] + j or self.queens[i + j] == self.queens[i] - j:
                        sum2 = 1
            
        if sum2 == 0:
            return f'Yes'
        else: 
            return f'No'

    def printBoard(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if self.queens[i] == j:
                    print(f'|X', end = '')
                else:
                    print(f'| ', end = '')
            print(f'|')
        

def main():
    board1 = EQ()
    board1.set(0, 2)
    board1.set(1, 4)
    board1.set(2, 7)
    board1.set(3, 1)
    board1.set(4, 0)
    board1.set(5, 3)
    board1.set(6, 6)
    board1.set(7, 5)
    print(f'Is board1 a correct eight queen placement? {board1.isSolved()}')

    board2 = EQ([0, 4, 7, 5, 2, 6, 1, 3])
    if board2.isSolved() == "Yes":
        print("Eight queens are placed correctly in board2")
        print()
    else:
        print("Eight queens are placed incorrectly in board2")

    f'{board2.printBoard()}'


main()
