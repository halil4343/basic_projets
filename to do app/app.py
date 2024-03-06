from customtkinter import * 
tasks = []
my_font = ("Terminal", 20)

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
    task_widget = CTkCheckBox(fr1, text=task, command=lambda: delete_task(task_widget, task),text_color='#DAF7A6',font=my_font)
    task_widget.pack(pady=5)
    update_task_file()
    

def add_task2():
    top = CTkToplevel(window)
    top.geometry("300x200+545+250")
    top.configure(fg_color="#581845")
    top.lift()
    top.focus_set()
    top.attributes('-topmost', True) 
    
    label2 = CTkLabel(top, text="Enter your task: ",text_color="#FFC300",corner_radius=100,font=("Terminal", 20))
    label2.pack()

    entry = CTkEntry(top, width=100,text_color="#FFC300",placeholder_text="Your task here",placeholder_text_color='#FFC300',font=("Terminal", 11))
    entry.pack()

    def add_task():
        task = entry.get()
        add_task1(task)
        top.destroy()

    ok_button = CTkButton(top, text="Ok", command=add_task,bg_color="#900C3F",fg_color='#C70039',font=my_font,text_color="#FFC300")
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
window.configure(fg_color="#581845")

the_font = ("MS Serif",25)

fr1 = CTkFrame(window, height=440, width=350,fg_color="#581845")
fr1.pack(pady=10) 

fr2 = CTkFrame(window, height=40, width=350)
fr2.pack(side=BOTTOM)

label1 = CTkLabel(fr1, text="To Do List",text_color="#FFC300",corner_radius=100,font=("Terminal", 30))
label1.pack(pady=10)

add_button = CTkButton(fr2, text="Add Task", command=add_task2,bg_color="#900C3F",fg_color='#C70039',font=my_font,text_color="#FFC300")
add_button.pack()

load_tasks()

window.mainloop()