from tkinter import *
from Calculator import Calculator

class CalculateIt: 
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator GUI")
        self.x = 45
        self.y = 35

        frame = Frame(self.window)
        frame.pack()
        operand1 =Label(frame, text = "Operand 1")
        operand2 =Label(frame, text = "Operator (+-*/")
        operand3 =Label(frame, text = "Operand 2")
        operand4 =Label(frame, text = "Result")
        operand1.grid(row = 1, column=1, sticky=W)
        operand2.grid(row = 2, column=1, sticky=W)
        operand3.grid(row = 3, column=1, sticky=W)
        operand4.grid(row = 4, column=1, sticky=W)

        self.operand1 = IntVar()
        input1 =Entry(frame, textvariable = self.operand1)
        self.operator = StringVar()
        input2 =Entry(frame, textvariable = self.operator)
        self.operand2 = IntVar()
        input3 =Entry(frame, textvariable = self.operand2)
        self.result = IntVar()
        showResult = Label(frame, textvariable=self.result)

        input1.grid(row=1, column=2)
        input2.grid(row=2, column=2)
        input3.grid(row=3, column=2)
        showResult.grid(row=4, column=2)

        btCalculate = Button(frame, text = "Calculate", command = self.calculate)
        btClearLog = Button(frame, text = "Clear log", command = self.clearLog)
        btQuit = Button(frame, text = "Quit", command = self.window.destroy)
        btCalculate.grid(row = 5, column=1)
        btClearLog.grid(row = 5, column=2)
        btQuit.grid(row = 5, column=3)


        self.canvas = Canvas(self.window, width = 200, height = 100, bg = "white")
        self.canvas.create_text(15, 15, text = "Log: ", fill = "black")
        self.canvas.pack()

        self.minicalculator = Calculator()

        self.window.mainloop()

    def calculate(self):
        number1 = float(self.operand1.get())
        number2 = float(self.operand2.get())
        operator = str(self.operator.get())
        answer = self.minicalculator.calculate(number1, number2, operator)
        self.result.set(format(answer, '10.2f'))
        self.canvas.create_text(self.x, self.y, text = f'{self.minicalculator.get_last_logged()}', tags = "text")
        self.y += 20

    def clearLog(self):
        self.minicalculator.clear_log()
        self.y = 35
        self.canvas.delete("text")

CalculateIt()
