from tkinter import *

class CanvasDemo: 
    def __init__(self):
        window = Tk()
        window.title("Move the ball")
        self.x = 40
        self.y = 40

        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()
        self.oval = self.canvas.create_oval(self.x, self.y, self.x + 15, self.y + 15, fill = "red", tags = "oval")
        
        frame = Frame(window)
        frame.pack()
        goLeft = Button(frame, text = "Left", command = self.goLeft)
        goRight = Button(frame, text = "Right", command = self.goRight)
        goUp = Button(frame, text = "Up", command = self.goUp)
        goDown = Button(frame, text = "Down", command = self.goDown)
        goLeft.grid(row=1, column=1)
        goRight.grid(row=1, column=2)
        goUp.grid(row=1, column=3)
        goDown.grid(row=1, column=4)

        window.mainloop()

    def goLeft(self):
        if self.x >= 5:
            self.canvas.move(self.oval, -5, 0)
            self.setX(5)
    
    def goRight(self):
        if self.x <= 185:
            self.canvas.move(self.oval, 5, 0)
            self.setX(-5)

    def goUp(self):
        if self.y >= 5:
            self.canvas.move(self.oval, 0, -5)
            self.setY(5)

    def goDown(self):
        if self.y <= 85: 
            self.canvas.move(self.oval, 0, 5)
            self.setY(-5)

    def setX(self, x):
        self.x = self.x - x

    def setY(self, y):
        self.y = self.y - y

        

CanvasDemo()