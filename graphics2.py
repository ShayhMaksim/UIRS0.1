from tkinter import *

root = Tk()
c = Canvas(width=300, height=300, bg='white')
c.focus_set()
c.pack()

ball = c.create_oval(140, 140, 160, 160, fill='green')
c.bind('<Up>', lambda event: c.move(ball, 0, -10))
c.bind('<Down>', lambda event: c.move(ball, 0, 10))
c.bind('<Left>', lambda event: c.move(ball, -10, 0))
c.bind('<Right>', lambda event: c.move(ball, 10, 0))

oval = c.create_oval(30, 10, 130, 80, tag="group1")
c.create_line(10, 100, 450, 100, tag="group1")


def color(event):
    c.itemconfig('group1', fill="red", width=3)


c.bind('<Button-3>', color)

root.mainloop()