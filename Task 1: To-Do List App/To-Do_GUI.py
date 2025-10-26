#ToDo List GUI
import tkinter as tk
import pickle
window=tk.Tk()
window.title("To-Do List Application")
window.geometry("500x650")
window.configure(bg="yellow")


def read():
    global data
    data=[]
    with open("Todo.dat","rb") as file:
        while True:
            try:
                row=pickle.load(file)
                data.extend(row)
            except:
                break
def add():
    task=entry.get()
    status=entry1.get()
    x=[[task,status]]
    with open("Todo.dat","ab") as file:
        pickle.dump(x,file)
    text.delete(1.0, tk.END)
    text.insert(tk.END, f" Task '{task}' added successfully.\n")

def show():
    read()
    display_text = "All Tasks:\n"
    for i in data:
        display_text += f"Task: {i[0]} | Status: {i[1]}\n"

    text.delete(1.0, tk.END)
    text.insert(tk.END, display_text)

def update():
    found=False
    task=entry.get()
    read()
    with open("Todo.dat","wb") as file:
        for i in data:
            if task != i[0]:
                x=[[i[0],i[1]]]
                pickle.dump(x,file)
            if task == i[0]:
                st=entry1.get()
                x=[[i[0],st]]
                pickle.dump(x,file)
                text.delete(1.0, tk.END)
                text.insert(tk.END,"Status changed\n")
                found=True
    if not found:
        text.delete(1.0, tk.END)
        text.insert(tk.END,"No records found\n")


def remove():
    task=entry.get()
    read()
    with open("Todo.dat","wb") as file:
        for i in data:
            if task != i[0]:
                x=[[i[0],i[1]]]
                pickle.dump(x,file)
    
    text.delete(1.0, tk.END)
    text.insert(tk.END,f"Task '{task}' removed (if it existed).\n")

    
def clear():
    entry.delete(0, tk.END)
    entry1.delete(0, tk.END)
    text.delete(1.0, tk.END)
    
label=tk.Label(window, text="To-Do List Application",font=("Arial",20), bg="lightblue")
label.pack(pady=20, fill="x")
label1=tk.Label(window, text="Task: ",font=("Arial",14), bg="lightgray")
label1.pack(pady=20, fill="x")
entry=tk.Entry(window)
entry.pack(pady=10, padx=40,ipady=5,fill="x")
label2=tk.Label(window, text="Status: ",font=("Arial",14), bg="lightgray")
label2.pack(pady=20, fill="x")
entry1=tk.Entry(window)
entry1.pack(pady=10, padx=40,ipady=5,fill="x")

button=tk.Button(window,text="add",command=add)
button.pack(pady=5)
button1=tk.Button(window,text="show",command=show)
button1.pack(pady=5)
button2=tk.Button(window,text="update",command=update)
button2.pack(pady=5)
button3=tk.Button(window,text="remove",command=remove)
button3.pack(pady=5)
button4=tk.Button(window,text="clear",command=clear)
button4.pack(pady=5)

text = tk.Text(window, height=5, wrap="word", font=("Arial", 12))
text.pack(padx=20, pady=10, fill="both", expand=True)

label4=tk.Label(window, text="Made by Sarthak Tyagi", font=("Arial",14), bg="lightgray")
label4.pack(fill="x", pady=5)
window.mainloop()