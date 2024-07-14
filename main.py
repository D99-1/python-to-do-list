import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"{task} (completed)")
    except:
        messagebox.showwarning("Warning", "You must select a task to complete.")

root = tk.Tk()
root.title("To-Do List")

task_frame = tk.Frame(root)
task_frame.pack(pady=10)

task_listbox = tk.Listbox(task_frame, width=50, height=10)
task_listbox.pack(side=tk.LEFT, padx=10)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, width=30)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(entry_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

action_frame = tk.Frame(root)
action_frame.pack(pady=10)

delete_button = tk.Button(action_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

complete_button = tk.Button(action_frame, text="Complete Task", command=complete_task)
complete_button.pack(side=tk.LEFT)

root.mainloop()
