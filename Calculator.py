class Calculator: 
    def __init__(self, operand1 = 0, operand2 = 0, operator = ""):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator
        self.log = []

    def calculate(self, x, y, z):
        self.operand1 = x
        self.operand2 = y 
        self.operator = z

        if self.operator == '+':
            result = self.operand1 + self.operand2
        elif self.operator == '*':
            result = self.operand1 * self.operand2
        elif self.operator == '/':
            result = self.operand1 / self.operand2
        elif self.operator == '-':
            result =  self.operand1 - self.operand2
        
        self.log.insert(len(self.log), f'{self.operand1} {self.operator} {self.operand2} = {result}')
        return result

    def get_log(self):
        return self.log

    def get_last_logged(self):
        return self.log[len(self.log)-1]

    def clear_log(self):
        self.log = []

def main():
    if __name__ == "__main__":
        calculator = Calculator()
        calculator.calculate(1, 2,'+')
        calculator.calculate(2, 2,'*')
        calculator.calculate(16, 2,'/')
        print(calculator.get_log())
        print(calculator.get_last_logged())

main()