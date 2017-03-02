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
        self.display.grid(row=0, column=0, columnspan=5)

        self.sevenButton = Button(self, font=("Helvetica", 11), text="7", borderwidth=1)
        self.sevenButton.grid(row=1, column=0, sticky="NWNESWSE")

        self.eightButton = Button(self, font=("Helvetica", 11), text="8", borderwidth=1)
        self.eightButton.grid(row=1, column=1, sticky="NWNESWSE")

        self.nineButton = Button(self, font=("Helvetica", 11), text="9", borderwidth=1)
        self.nineButton.grid(row=1, column=2, sticky="NWNESWSE")

        self.timesButton = Button(self, font=("Helvetica", 11), text="*", borderwidth=1)
        self.timesButton.grid(row=1, column=3, sticky="NWNESWSE")

        self.clearButton = Button(self, font=("Helvetica", 11), text="C", borderwidth=1)
        self.clearButton.grid(row=1, column=4, sticky="NWNESWSE")


app = Application(root).grid()
root.mainloop()
