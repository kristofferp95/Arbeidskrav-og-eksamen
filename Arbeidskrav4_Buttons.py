from tkinter import *

class Radio: 
    def __init__(self):
        window = Tk()
        window.title("Radio buttons and buttons")
        self.x = 150
        self.y = 50

        frame = Frame(window)
        frame.pack()
        self.v1 = StringVar()
        rbRed = Radiobutton(frame, text = "Red", variable = self.v1, value = "R", command = self.processRadiobutton)
        rbYellow = Radiobutton(frame, text = "Yellow", variable = self.v1, value = "Y", command = self.processRadiobutton)
        rbWhite = Radiobutton(frame, text = "White", variable = self.v1, value = "W", command = self.processRadiobutton)
        rbGray = Radiobutton(frame, text = "Gray", variable = self.v1, value = "G", command = self.processRadiobutton)
        rbGreen = Radiobutton(frame, text = "Green", variable = self.v1, value = "GR", command = self.processRadiobutton)
        rbRed.grid(row=1, column =1)
        rbYellow.grid(row=1, column =2)
        rbWhite.grid(row=1, column =3)
        rbGray.grid(row=1, column =4)
        rbGreen.grid(row=1, column =5)

        self.canvas = Canvas(window, width = 300, height = 100, bg = "White")
        self.canvas.pack()
        self.text = self.canvas.create_text(self.x, self.y, text = "Welcome", fill = "black")

        frame2 = Frame()
        frame2.pack()
        btnLeft = Button(frame2, text = "<=", command = self.goLeft)
        btnRight = Button(frame2, text = "=>", command = self.goRight)
        btnLeft.grid(row = 1, column=1)
        btnRight.grid(row = 1, column = 2)

        window.mainloop()

    def goLeft(self):
        if self.x > 25:
            self.canvas.move(self.text, -5, 0)
            self.setX(5)
    
    def goRight(self):
        if self.x < 275:
            self.canvas.move(self.text, 5, 0)
            self.setX(-5)

    def setX(self, x):
        self.x = self.x - x

    def processRadiobutton(self): 
        if self.v1.get() == "R":
            self.canvas["bg"] = "red"
        elif self.v1.get() == "Y":
            self.canvas["bg"] = "yellow"
        elif self.v1.get() == "W":
            self.canvas["bg"] = "white"
        elif self.v1.get() == "G":
            self.canvas["bg"] = "gray"
        elif self.v1.get() == "GR":
            self.canvas["bg"] = "green"


Radio()

