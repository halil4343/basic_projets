from tkinter import *

def addTask1(task):
    task1 = Checkbutton(fr1, text=task, width=300, background="aqua", command=lambda: delete(task1))
    task1.pack()
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def delete(widget):
    widget.destroy()

def addTask2():
    top = Toplevel(window)
    top.geometry("300x200+545+250")

    label2 = Label(top, text="Enter your task: ")
    label2.pack()

    entry = Entry(top, width=40)
    entry.pack()

    def add_task():
        task = entry.get()
        addTask1(task)
        top.destroy()

    ok_button = Button(top, text="Ok", command=add_task)
    ok_button.pack(side=BOTTOM)

try:
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            addTask1(task.strip())  # Strip whitespace and newline characters
except FileNotFoundError:
    pass

window = Tk()
window.title("To Do")
window.geometry("400x500+500+150")

fr1 = Frame(window, height=440, width=350)
fr1.pack()

fr2 = Frame(window, height=40, width=350)
fr2.pack(side=BOTTOM)

label1 = Label(fr1, text="To Do List")
label1.pack()

add_button = Button(fr2, text="Add Task", command=addTask2)
add_button.pack()

window.mainloop()
