#Game GUI
import tkinter as tk
import random
L=["1","2","3"]
D={"1":"Rock","2":"Paper","3":"Scissors"}
user=0
comp=0
window=tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("700x750")
window.configure(bg="yellow")

def game():
    global user, comp
    try:
        C=D[random.choice(L)]
#         print(C)
        n=D[(entry.get())]
#         print(n)
        if entry.get() in L:
            if C==n:
                label4.config(text=f"Both choose {C}, it's a draw")
            elif n=="Rock":
                if C=="Paper":
                    label4.config(text=f"Computer has {C}, you lose")
                    comp+=1
                else:
                    label4.config(text=f"Computer has {C}, you win")
                    user+=1
            elif n=="Scissors":
                if C=="Rock":
                    label4.config(text=f"Computer has {C}, you lose")
                    comp+=1
                else:
                    label4.config(text=f"Computer has {C}, you win")
                    user+=1
            elif n=="Paper":
                if C=="Scissors":
                    label4.config(text=f"Computer has {C}, you lose")
                    comp+=1
                else:
                    label4.config(text=f"Computer has {C}, you win")
                    user+=1

    except:
        label4.config(text="Not valid a choice")
    label1.config(text=f"Your Points: {user}")
    label2.config(text=f"Computer's Points: {comp}")

def clear():
    entry.delete(0, tk.END)

label=tk.Label(window, text="Let's Play Rock-Paper-Scissors", font=("Arial", 20),bg="lightblue")
label.pack(pady=20, fill="x")
label5=tk.Label(window, text="Enter your choice\n1. Rock\n2. Paper\n3. Scissors", font=("Arial", 20),bg="yellow")
label5.pack(pady=20, fill="x")
entry=tk.Entry(window)
entry.pack(pady=10, padx=40,ipady=5)
button=tk.Button(window,text="Submit",command=game)
button.pack(pady=10)
button1=tk.Button(window,text="clear",command=clear)
button1.pack(pady=5)
label4=tk.Label(window, text="Results", font=("Arial", 20),bg="lightblue")
label4.pack(pady=20, fill="x")
label1=tk.Label(window, text="Your Points: 0", font=("Arial", 20),bg="lightgreen")
label1.pack(pady=20, fill="x")
label2=tk.Label(window, text="Computer's Points: 0", font=("Arial", 20),bg="red")
label2.pack(pady=20, fill="x")

label3=tk.Label(window, text="Made by Sarthak Tyagi", font=("Arial",14), bg="lightgray")
label3.pack(fill="x", pady=5)
window.mainloop()