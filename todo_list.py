from tkinter import *
from tkinter import messagebox

def ADD():
    task = task_entry.get()
    if task:
        task_list.insert(END, task)
        task_entry.delete(0,END)
    else:
        messagebox.showwarning("Warning !!", "Please enter a task !!")

def REMOVE():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning !!", "Please select a task to remove !!")

def CLEAR():
    task_list.delete(0,END)


root =Tk()
root.title("To-Do List")

task_entry = Entry(root, width=40,bg="grey",fg="white")
task_entry.pack(pady=5)

task_list = Listbox(root, width=40, height=15)
task_list.pack()

add_button = Button(root, text="ADD",width=10,  command=ADD,bg="grey",relief="groove",fg="white")
add_button.pack(side=LEFT,padx=1.5)

remove_button = Button(root, text="REMOVE",width=10, command=REMOVE,bg="red",relief="groove",fg="blue")
remove_button.pack(side=LEFT,padx=1.)

clear_button = Button(root, text="CLEAR ALL",width=10, command=CLEAR,bg="yellow",relief="groove",fg="blue")
clear_button.pack(side=LEFT,padx=2)


root.mainloop()

