# Todo
import pickle
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
#         return data
        
def add():
    task=input("Enter task: ")
    status=input("Enter status: ")
    x=[[task,status]]
    with open("Todo.dat","ab") as file:
        pickle.dump(x,file)
        print(f"Task {task} added successfully.\n")
        
def display():
    read()
    print("All Tasks\n")
    for i in data:
        
        print(f"Task: {i[0]} | Status: {i[1]}\n")
        
def remove():
    task=input("Enter task to remove: ")
    read()
    with open("Todo.dat","wb") as file:
        for i in data:
            if task != i[0]:
                x=[[i[0],i[1]]]
                pickle.dump(x,file)
        print(f"Task {task} removed (if existed)\n")
            
def update():
    found=False
    task=input("Enter task to update status: ")
    read()
    with open("Todo.dat","wb") as file:
        for i in data:
            if task != i[0]:
                x=[[i[0],i[1]]]
                pickle.dump(x,file)
            if task == i[0]:
                st=input("Enter status: ")
                x=[[i[0],st]]
                pickle.dump(x,file)
                print("Status changed\n")
                found=True
    if not found:
        print("No records found\n")
        
while True:
    print("\n---To-Do List Application---\n")
    n=input("1. Add\n2. Display\n3. Update\n4. Remove\n5. exit\n")
    if n=="5":
        print("Exit")
        break
    elif n=="1":
        add()
    elif n=="2":
        display()
    elif n=="3":
        update()
    elif n=="4":
        remove()
    else:
        print("Invalid choice. Please enter 1-5.\n")
        