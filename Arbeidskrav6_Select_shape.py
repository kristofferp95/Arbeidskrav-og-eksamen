from tkinter import *

class SelectShapes:
    def __init__(self):
        window = Tk()
        window.title("Select Shapes")

        self.var = StringVar()
        self.var.set("Pick your shape")
        combobox = OptionMenu(window, self.var, "Rectangle", "Oval", "Arc", "Polygon", "line", command = self.processSelection).pack(fill=BOTH)

        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()

        window.mainloop()

    def processSelection(self, selecteditem):
        self.canvas.delete("rectangle", "oval", "arc", "polygon", "line")
        if selecteditem == "Rectangle":
            self.canvas.create_rectangle(10, 10, 190, 90, tags = "rectangle")
        elif selecteditem == "Oval":
            self.canvas.create_oval(10, 10, 190, 90, fill = "red", tags= "oval")
        elif selecteditem == "Arc":
            self.canvas.create_arc(10, 10, 190, 90, start = 0, extent = 90, width = 7, fill = "red", tags = "arc")
        elif selecteditem == "Polygon":
            self.canvas.create_polygon(10, 10, 190, 90, 30, 50, tags = "polygon")
        elif selecteditem == "line":
            self.canvas.create_line(10, 10, 190, 90, fill = "red", tags = "line")


SelectShapes()