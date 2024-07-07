import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Create a list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Create UI components with styling
frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40, font=('Arial', 14))
task_entry.pack(side=tk.LEFT, padx=(0, 10))

add_button = tk.Button(frame, text="Add Task", command=add_task, bg="#007BFF", fg="white", font=('Arial', 12), padx=10, pady=5)
add_button.pack(side=tk.LEFT)

task_list_frame = tk.Frame(root, bg="#f0f0f0")
task_list_frame.pack(pady=10)

task_listbox = tk.Listbox(task_list_frame, width=50, height=10, font=('Arial', 12), bd=0, selectbackground="#ff6347", activestyle="none")
task_listbox.pack(side=tk.LEFT)

# Add a scrollbar to the listbox
scrollbar = tk.Scrollbar(task_list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#dc3545", fg="white", font=('Arial', 12), padx=10, pady=5)
delete_button.pack(pady=10)

# Start the main event loop
root.mainloop()
