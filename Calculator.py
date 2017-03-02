from tkinter import *

root = Tk()
root.title = "Calculator"
root.resizable(0, 0)


class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.createWidgets()

    def createWidgets(self):
        self.display = Entry(self, font=("Helvetica", 16), relief=RAISED, justify=RIGHT)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0)


app = Application(root).grid()
root.mainloop()
