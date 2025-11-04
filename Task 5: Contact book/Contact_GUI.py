#Contbook GUI
import tkinter as tk
import pickle
window=tk.Tk()
window.title("CONTACT BOOK")
window.geometry("500x650")
window.configure(bg="yellow")

def read():
    global data
    data=[]
    with open("Contact.dat","rb") as file:
        while True:
            try:
                row=pickle.load(file)
                data.extend(row)
            except:
                break

def add():
    n=entry.get()
    c=entry1.get()
    x=[[n,c]]
    with open("Contact.dat","ab") as file:
        pickle.dump(x,file)
    text.delete(1.0, tk.END)
    text.insert(tk.END, f" Contact '{n}' added successfully.\n")

def show(): 
    read()
    display = "All Contacts:\n"
    for i in data:
        display += f"Name: {i[0]} | Number: {i[1]}\n"

    text.delete(1.0, tk.END)
    text.insert(tk.END, display)

def search():
    n = entry.get()
    found = False
    read()
    for i in data:
        if n == i[0]:
            text.delete(1.0, tk.END)
            text.insert(tk.END, f"Name: {i[0]} | Contact: {i[1]}")
            found = True
    if not found:
        text.delete(1.0, tk.END)
        text.insert(tk.END,"Contact not found.\n")

def remove():
    n=entry.get()
    read()
    with open("Contact.dat","wb") as file:
        for i in data:
            if n != i[0]:
                x=[[i[0],i[1]]]
                pickle.dump(x,file)
    
    text.delete(1.0, tk.END)
    text.insert(tk.END,f"Contact '{n}' removed (if it existed).\n")

    
def clear():
    entry.delete(0, tk.END)
    entry1.delete(0, tk.END)
    text.delete(1.0, tk.END)
    
label=tk.Label(window, text="Contact Book",font=("Arial",20), bg="lightblue")
label.pack(pady=20, fill="x")
label1=tk.Label(window, text="Name: ",font=("Arial",14), bg="lightgray")
label1.pack(pady=20, fill="x", padx=40)
entry=tk.Entry(window)
entry.pack(pady=10, padx=40,ipady=5,fill="x")
label2=tk.Label(window, text="Number: ",font=("Arial",14), bg="lightgray")
label2.pack(pady=20, fill="x", padx=40)
entry1=tk.Entry(window)
entry1.pack(pady=10, padx=40,ipady=5,fill="x")

button=tk.Button(window,text="add",command=add)
button.pack(pady=5)
button1=tk.Button(window,text="search",command=search)
button1.pack(pady=5)
button2=tk.Button(window,text="show all",command=show)
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