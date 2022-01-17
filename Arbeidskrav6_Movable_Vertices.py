from tkinter import *
import math

class Circle:
    def __init__(self, x = 0, y = 0, radius = 20):
        self.x = x
        self.y = y
        self.radius = radius

    def inSide(self, x, y):
        if math.sqrt((self.x - x)**2 + (self.y - y)**2) <= 20: 
            return True

class Twocircles():
    def __init__(self):
        window = Tk()
        window.title("Two circles")

        self.canvas = Canvas(window, width = 200, height = 150, bg="white")
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.mouseMoved)
        
        self.circle1 = Circle(20, 20, 20)
        self.canvas.create_oval(self.circle1.x - self.circle1.radius, self.circle1.y-self.circle1.radius, 
        self.circle1.x + self.circle1.radius, self.circle1.y + self.circle1.radius, fill="red", tags="circle1")
        
        self.circle2 = Circle(120, 50, 20)
        self.canvas.create_oval(self.circle2.x-self.circle2.radius, self.circle2.y-self.circle2.radius, 
        self.circle2.x+self.circle2.radius, self.circle2.y+self.circle2.radius, fill="red", tags="circle2")
        
        self.line = self.canvas.create_line(self.circle1.x, self.circle1.y, self.circle2.x, self.circle2.y, tags="line")
        self.distance = math.sqrt((self.circle2.x-self.circle1.x)**2 + (self.circle2.y-self.circle1.y)**2)
        
        placex = (self.circle1.x + self.circle2.x) / 2
        placey = (self.circle1.y + self.circle2.y) / 2
        self.text = self.canvas.create_text(placex, placey, text = f'{self.distance:.2f}', fill="black", tags="text")

        window.mainloop()

    def mouseMoved(self, event):
        if self.circle1.inSide(event.x, event.y) == True and self.distance > 70.0:
            self.canvas.delete("circle1", "text", "line" )
            self.circle1.x = event.x
            self.circle1.y = event.y
            self.canvas.create_oval(self.circle1.x - self.circle1.radius, self.circle1.y-self.circle1.radius, 
            self.circle1.x + self.circle1.radius, self.circle1.y + self.circle1.radius, fill="red", tags="circle1")
            
            self.line = self.canvas.create_line(self.circle1.x, self.circle1.y, self.circle2.x, self.circle2.y, tags="line")
            self.distance = math.sqrt((self.circle2.x-self.circle1.x)**2 + (self.circle2.y-self.circle1.y)**2)
            placex = (self.circle1.x + self.circle2.x) / 2
            placey = (self.circle1.y + self.circle2.y) / 2
            self.text = self.canvas.create_text(placex, placey, text = f'{self.distance:.2f}', fill="black", tags="text")

        elif self.circle2.inSide(event.x, event.y) == True and self.distance > 70.0:
            self.canvas.delete("circle2", "text", "line" )
            self.circle2.x = event.x
            self.circle2.y = event.y
            self.canvas.create_oval(self.circle2.x - self.circle2.radius, self.circle2.y-self.circle1.radius, 
            self.circle2.x + self.circle2.radius, self.circle2.y + self.circle2.radius, fill="red", tags="circle2")
            
            self.line = self.canvas.create_line(self.circle1.x, self.circle1.y, self.circle2.x, self.circle2.y, tags="line")
            self.distance = math.sqrt((self.circle2.x-self.circle1.x)**2 + (self.circle2.y-self.circle1.y)**2)
            placex = (self.circle1.x + self.circle2.x) / 2
            placey = (self.circle1.y + self.circle2.y) / 2
            self.text = self.canvas.create_text(placex, placey, text = f'{self.distance:.2f}', fill="black", tags="text")

        #Denne ble lagt inn fordi B1 motion inkrementerer slik at den kan komme under 70 pixel. 
        #På denne måten stopper ikke simuleringen opp, men går tilbake til start.
        elif self.distance < 70:
            self.canvas.delete("circle1","circle2", "text", "line" )
            self.circle1 = Circle(20, 20, 20)
            self.canvas.create_oval(self.circle1.x - self.circle1.radius, self.circle1.y-self.circle1.radius, 
            self.circle1.x + self.circle1.radius, self.circle1.y + self.circle1.radius, fill="red", tags="circle1")
        
            self.circle2 = Circle(120, 50, 20)
            self.canvas.create_oval(self.circle2.x-self.circle2.radius, self.circle2.y-self.circle2.radius, 
            self.circle2.x+self.circle2.radius, self.circle2.y+self.circle2.radius, fill="red", tags="circle2")
        
            self.line = self.canvas.create_line(self.circle1.x, self.circle1.y, self.circle2.x, self.circle2.y, tags="line")
            self.distance = math.sqrt((self.circle2.x-self.circle1.x)**2 + (self.circle2.y-self.circle1.y)**2)
        
            placex = (self.circle1.x + self.circle2.x) / 2
            placey = (self.circle1.y + self.circle2.y) / 2
            self.text = self.canvas.create_text(placex, placey, text = f'{self.distance:.2f}', fill="black", tags="text")


Twocircles()