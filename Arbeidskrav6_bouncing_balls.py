from tkinter import *
from random import randint

def getRandomcolor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15))
    return color

def toHexChar(hexValue):
    if 0 <= hexValue <=9:
        return chr(hexValue + ord('0'))
    else: 
        return chr(hexValue - 10 + ord('A'))


class Ball: 
    def __init__(self):
        self.x = 0 
        self.y = 0
        self.dx = 2
        self.dy = 2
        self.radius = 3 
        self.color = getRandomcolor()
    

class BounceBalls(Ball): 
    def __init__(self):
        self.ballList = []

        self.window = Tk()
        self.window.title("Bouncing balls")

        self.window.protocol("VM_DELETE_WINDOW", self.quit)

        self.width = 350
        self.height = 150
        self.canvas = Canvas(self.window, bg = "white", width = self.width, height = self.height)
        self.canvas.pack()

        frame = Frame(self.window)
        frame.pack()
        btStop = Button(frame, text = "stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "resume", command = self.resume)
        btResume.pack(side = LEFT)
        btAdd = Button(frame, text = "+", command = self.add)
        btAdd.pack(side = LEFT)
        btRemove = Button(frame, text = "-", command = self.remove)
        btRemove.pack(side = LEFT)
        btfaster = Button(frame, text = "Faster", command =self.faster)
        btfaster.pack(side=LEFT)
        btslower = Button(frame, text="Slower", command = self.slower)
        btslower.pack(side=LEFT)

        self.sleeptime = 100
        self.isstopped = False
        self.animate()

        self.window.mainloop()
    
    def slower(self):
        for ball in self.ballList:
            if ball.dx > 1 and ball.dy > 1:
                ball.dx -=1
                ball.dy -=1
            elif ball.dx > 1 and ball.dy < -1:
                ball.dx -=1
                ball.dy +=1
            elif ball.dx < -1 and ball.dy > 1:
                ball.dx +=1
                ball.dy -=1
            elif ball.dx < -1 and ball.dy < -1:
                ball.dx += 1
                ball.dy += 1
    
    def faster(self):
        for ball in self.ballList:
            if ball.dx > 0 and ball.dy > 0:
                ball.dx +=1
                ball.dy +=1
            elif ball.dx > 0 and ball.dy < 0:
                ball.dx +=1
                ball.dy -=1
            elif ball.dx < 0 and ball.dy > 0:
                ball.dx -=1
                ball.dy +=1
            else: 
                ball.dx -= 1
                ball.dy -= 1

    def stop(self):
        self.isstopped = True
    
    def resume(self):
        self.isstopped = False
        self.animate()

    def add(self):
        self.ballList.append(Ball())
    
    def remove(self):
        self.ballList.pop()
    
    def animate(self):
        while not self.isstopped:
            self.canvas.delete("ball")

            for ball in self.ballList:
                self.redisplayBall(ball)
            
            self.canvas.after(self.sleeptime)
            self.canvas.update()
    
    def redisplayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx
        
        if ball.y > self.height or ball.y < 0: 
            ball.dy = -ball.dy
        
        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius, \
            ball.x + ball.radius, ball.y + ball.radius, fill = ball.color, tags = "ball")
    
    def quit(self):
        self.stop()
        self.window.destroy()

BounceBalls()
