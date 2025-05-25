import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        deleted_listbox.insert(tk.END, task)
        task_listbox.delete(selected)

def mark_task():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        done_listbox.insert(tk.END, task)
        task_listbox.delete(selected)

def edit_task(event):
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        old_text = task_listbox.get(index)

        # Всплывающее окно редактирования
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Task")
        edit_window.geometry("300x100")
        edit_window.configure(bg="#f0f0f0")

        entry = tk.Entry(edit_window, width=40)
        entry.insert(0, old_text)
        entry.pack(pady=10)

        def save_edit():
            new_text = entry.get()
            if new_text:
                task_listbox.delete(index)
                task_listbox.insert(index, new_text)
                edit_window.destroy()

        save_button = tk.Button(edit_window, text="Сохранить", command=save_edit, bg="#90be6d")
        save_button.pack()

root = tk.Tk()
root.title("To-Do List")
root.configure(background="#e6e6fa", padx=10, pady=10)

entry_frame = tk.Frame(root, bg="#e6e6fa")
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, width=40, font=('Arial', 12))
task_entry.pack(side=tk.LEFT, padx=(0, 10))

add_task_button = tk.Button(entry_frame, text="Add Task", bg="#8ecae6", fg="black", command=add_task)
add_task_button.pack(side=tk.LEFT)

button_frame = tk.Frame(root, bg="#e6e6fa")
button_frame.pack(pady=10)

delete_button = tk.Button(button_frame, text="Delete Task", bg="#f4a261", command=delete_task)
delete_button.grid(row=0, column=0, padx=10)

mark_button = tk.Button(button_frame, text="Mark as Done", bg="#90be6d", command=mark_task)
mark_button.grid(row=0, column=1, padx=10)

list_frame = tk.Frame(root, bg="#e6e6fa")
list_frame.pack(pady=10)

task_frame = tk.Frame(list_frame, bg="#e6e6fa")
task_frame.pack(side=tk.LEFT, padx=10)

tk.Label(task_frame, text="To-Do", bg="#e6e6fa", font=('Arial', 12, 'bold')).pack()
task_listbox = tk.Listbox(task_frame, height=10, width=30, bg="#e0fbfc", font=('Arial', 10))
task_listbox.pack()

done_frame = tk.Frame(list_frame, bg="#e6e6fa")
done_frame.pack(side=tk.LEFT, padx=10)

tk.Label(done_frame, text="Done", bg="#e6e6fa", font=('Arial', 12, 'bold')).pack()
done_listbox = tk.Listbox(done_frame, height=10, width=30, bg="#d8f3dc", font=('Arial', 10))
done_listbox.pack()

task_listbox.bind("<Double-Button-1>", edit_task)

deleted_frame = tk.Frame(list_frame, bg="#e6e6fa")
deleted_frame.pack(side=tk.LEFT, padx=10)

tk.Label(deleted_frame, text="Deleted", bg="#e6e6fa", font=('Arial', 12, 'bold')).pack()
deleted_listbox = tk.Listbox(deleted_frame, height=10, width=30, bg="#ffcad4", font=('Arial', 10))
deleted_listbox.pack()

root.mainloop()
