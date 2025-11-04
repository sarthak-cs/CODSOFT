#Contact book
import pickle
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
#         return data
        
def add():
    n=input("Enter Name: ")
    c=input("Enter Number: ")
    e= input("Enter E-mail: ")
    a= input("Enter address: ")
    x=[[n,c,e,a]]
    with open("Contact.dat","ab") as file:
        pickle.dump(x,file)
        print(f"Contact {n} added successfully.\n")
        
def display():
    read()
    print("All Contacts\n")
    for i in data:
        
        print(f"Name: {i[0]} | Number: {i[1]} | E-mail: {i[2]} | Address: {i[3]}\n")
        
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
            
def search():
    found=False
    n=input("Enter Name to search contact: ")
    read()
    for i in data:
        if n == i[0]:
            print(f"Name: {i[0]} | Number: {i[1]} | E-mail: {i[2]} | Address: {i[3]}\n")
            found=True
    if not found:
        print("No records found\n")
        
while True:
    print("\n---Contact Book---\n")
    n=input("1. Add\n2. Display\n3. Search\n4. Remove\n5. exit\n")
    if n=="5":
        print("Exit")
        break
    elif n=="1":
        add()
    elif n=="2":
        display()
    elif n=="3":
        search()
    elif n=="4":
        remove()
    else:
        print("Invalid choice. Please enter 1-5.\n")
        