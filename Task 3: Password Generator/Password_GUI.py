#Password GUI
import tkinter as tk
import random
window=tk.Tk()
window.title("Password Generator")
window.geometry("400x400")
window.configure(bg="yellow")
def password():
    try:
        x=int(entry.get())
        letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        digit=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        sp_char=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

        passwd=""
        for i in range(x):
            passwd=passwd+random.choice(letter+digit+sp_char)
        label2.config(state="normal")       
        label2.delete(0, tk.END)            
        label2.insert(0, passwd)            
        label2.config(state="readonly")   
    
    except ValueError:
        label2.config(state="normal")       
        label2.delete(0, tk.END)            
        label2.insert(0, "Enter number only")            
        label2.config(state="readonly") 

label1=tk.Label(window, text="Enter length of the Password", font=("Arial",20), bg="lightblue")
label1.pack(pady=20, fill="x")

entry=tk.Entry(window)
entry.pack(pady=10, padx=40,ipady=5)

button=tk.Button(window,text="Generate Password",command=password)
button.pack(pady=10)

label3=tk.Label(window, text="The Generated Password is:", font=("Arial",20), bg="lightgreen")
label3.pack(fill="x", pady=20)

label2 = tk.Entry(window, font=("Arial", 20), justify="center", state="readonly")
label2.pack(pady=20, fill="x", padx=20)


label4=tk.Label(window, text="Made by Sarthak Tyagi", font=("Arial",14), bg="lightgray")
label4.pack(fill="x", pady=10)
    
window.mainloop()