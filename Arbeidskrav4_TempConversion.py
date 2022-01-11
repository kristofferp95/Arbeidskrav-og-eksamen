from tkinter import *

class Fahrenheit: 
    def __init__(self):
        window = Tk()
        window.title("Temp conversion")

        Label(window, text = "Input Celsius degrees").grid(row = 1, column = 1, sticky=W)
        Label(window, text = "degrees in Fahrenheit").grid(row = 2, column = 1, sticky=W)
        
        self.celsius = StringVar()
        Entry(window, textvariable = self.celsius, justify = RIGHT).grid(row = 1, column = 2)
        self.fahrenheit = StringVar()
        lblFahrenheit = Label(window, textvariable = self.fahrenheit).grid(row = 2, column = 2, sticky=E)
        btConvert = Button(window, text = "Convert", command = self.conversion).grid(row = 3, column=2, sticky=E)

        window.mainloop()

    def conversion(self):
        fahrenheit = (float(self.celsius.get()) *9 / 5) + 32
        self.fahrenheit.set(format(fahrenheit, '10.2f'))

Fahrenheit()

