import tkinter as tk
from tkinter import simpledialog, messagebox

def add_task():
    task = simpledialog.askstring("Task", "Enter a task:")
    if task:
        listbox.insert(tk.END, task)

def delete_task(event):
    selection = listbox.curselection()
    if selection:
        listbox.delete(selection[0])

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Bunnell-ToDo")

# Menu Bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0, background="#66ccff", foreground="#003366")
file_menu.add_command(label="Add Task", command=add_task)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Scrollbar and Listbox
frame = tk.Frame(root)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
listbox = tk.Listbox(frame, height=10, width=40, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
frame.pack()

# Instructions Label
instruction = tk.Label(root, text="Right-click on a task to delete it.", fg="green")
instruction.pack()

# Bind right-click to delete function
listbox.bind("<Button-3>", delete_task)  # Button-3 is right-click

root.mainloop()
