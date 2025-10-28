#Calculator GUI
import tkinter as tk
window=tk.Tk()
window.title("Simple Calculator")
window.geometry("500x550")
window.configure(bg="yellow")

def clear():
    entry.delete(0, tk.END)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label2.config(text="...", bg="red")
    

def calc():
    try:
        res=0
        if entry2.get()=="+":
            res=float(entry.get())+float(entry1.get())
        elif entry2.get()=="-":
            res=float(entry.get())-float(entry1.get())
        elif entry2.get()=="*":
            res=float(entry.get())*float(entry1.get())
        elif entry2.get()=="/":
            res=float(entry.get())/float(entry1.get())
        else:
            res="This isn't allowed"

        label2.config(text=f"{res}", bg="lightgreen", wraplength=450)   
    except ZeroDivisionError:
        label2.config(text="Can not divide by Zero", bg="lightgreen", wraplength=450)
    except:
        label2.config(text="This isn't allowed", bg="lightgreen", wraplength=450)
    
label1=tk.Label(window, text="This is a Calculator\nYou may write an operation in the given box", font=("Arial",14), bg="lightblue")
label1.pack(pady=20, fill="x")

label3=tk.Label(window, text="Enter First number", font=("Arial",14), bg="yellow")
label3.pack()
entry=tk.Entry(window)
entry.pack(pady=10, padx=40, fill="x",ipady=5)
label5=tk.Label(window, text="Enter the operation (+ , - , * , /)", font=("Arial", 14), bg="yellow")
label5.pack()
entry2=tk.Entry(window)
entry2.pack(pady=10, padx=40, fill="x", ipady=5)
label4=tk.Label(window, text="Enter Second number", font=("Arial",14), bg="yellow")
label4.pack()
entry1=tk.Entry(window)
entry1.pack(pady=10, padx=40, fill="x", ipady=5)

button=tk.Button(window,text="Submit",command=calc)
button.pack(pady=10)

button=tk.Button(window,text="Clear",command=clear)
button.pack(pady=10)

label2=tk.Label(window, text="...", font=("Arial",20), bg="red")
label2.pack(pady=20, fill="x",expand="True")

label6=tk.Label(window, text="Made by Sarthak Tyagi", font=("Arial",14), bg="lightgray")
label6.pack(fill="x", pady=10)
window.mainloop()