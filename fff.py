from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
frame2 = Frame(root)
frame2.pack(side=BOTTOM)

button = Button(frame, text = "Ok", fg="red")
button2 = Button(frame, text = "Cancel", fg="blue")
label = Label(root, text = "Exit", bg="blue", fg="white")

button.pack(side=LEFT)
button2.pack(side=RIGHT)
label.pack(fill=X)

canvas = Canvas(root, width="400", height="400")
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")
circle = canvas.create_oval(100, 100, 50, 50)
canvas.delete(ALL)
print("Hello world")
root.mainloop()

