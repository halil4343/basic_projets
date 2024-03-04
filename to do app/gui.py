from tkinter import *
path = "C:/Users/Ozerh/Desktop/basic_projets/tasks.txt"
tasks = []

def delete_text_from_file(text_to_delete):
    text_to_delete = text_to_delete + "\n"
    # Read the contents of the file
    with open("tasks.txt", "r") as file:
        lines = file.readlines()

    # Remove lines containing the specified text
    modified_lines = [line for line in lines if text_to_delete not in line]

    # Write the modified contents back to the file
    with open("tasks.txt", "w") as file:
        file.writelines(modified_lines)

def delete_task(task_widget,text_to_delete):
    tasks.remove(text_to_delete)
    delete_text_from_file(text_to_delete)
    task_widget.destroy()
    update_task_file()

def update_task_file():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task1(task):
    tasks.append(task)
    task_widget = Checkbutton(fr1, text=task, command=lambda: delete_task(task_widget, task))
    task_widget.pack()
    update_task_file()

def add_task2():
    top = Toplevel(window)
    top.geometry("300x200+545+250")

    label2 = Label(top, text="Enter your task: ")
    label2.pack()

    entry = Entry(top, width=40)
    entry.pack()

    def add_task():
        task = entry.get()
        add_task1(task)
        top.destroy()

    ok_button = Button(top, text="Ok", command=add_task)
    ok_button.pack(side=BOTTOM)

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                add_task1(task.strip())
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

add_button = Button(fr2, text="Add Task", command=add_task2)
add_button.pack()

load_tasks()

window.mainloop()
