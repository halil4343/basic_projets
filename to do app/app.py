from customtkinter import *
import pyglet, os
path = "C:/Users/Ozerh/Desktop/basic_projets/tasks.txt"
tasks = []


def delete_text_from_file(text_to_delete):
    text_to_delete = text_to_delete + "\n"
    with open("tasks.txt", "r") as file:
        lines = file.readlines()
        
    modified_lines = [line for line in lines if text_to_delete not in line]

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
            if task.strip():
                file.write(task + "\n")

def add_task1(task):
    tasks.append(task)
    task_widget = CTkCheckBox(fr1, text=task, command=lambda: delete_task(task_widget, task))
    task_widget.pack()
    update_task_file()
    

def add_task2():
    top = CTkToplevel(window)
    top.geometry("300x200+545+250")
    top.lift()
    top.focus_set()
    top.attributes('-topmost', True) 
    
    label2 = CTkLabel(top, text="Enter your task: ")
    label2.pack()

    entry = CTkEntry(top, width=40)
    entry.pack()

    def add_task():
        task = entry.get()
        add_task1(task)
        top.destroy()

    ok_button = CTkButton(top, text="Ok", command=add_task)
    ok_button.pack(side=BOTTOM)

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                if task.strip():
                    add_task1(task.strip())
    except FileNotFoundError:
        pass

window = CTk()
window.title("To Do")
window.geometry("400x500+500+150")

the_font = ("MS Serif",25)

fr1 = CTkFrame(window, height=440, width=350)
fr1.pack()

fr2 = CTkFrame(window, height=40, width=350)
fr2.pack(side=BOTTOM)

label1 = CTkLabel(fr1, text="To Do List",font=the_font)
label1.pack()

add_button = CTkButton(fr2, text="Add Task", command=add_task2,font=the_font)
add_button.pack()

load_tasks()

window.mainloop()
