#Game
import random
L=["Rock","Paper","Scissors"]
user=0
comp=0
while True:
    print(f"\nYour points: {user} and Computer points: {comp}\n")
    C=random.choice(L).capitalize()
    # print(C)
    n=input("Rock, Paper or Scissors (Or press 0 if you want to quit): ").capitalize()
    print("\n")
    if n in L:
        if C==n:
            print(f"Both choose {C}, it's a draw")
        elif n=="Rock":
            if C=="Paper":
                print(f"Computer has {C}, you lose")
                comp+=1
            else:
                print(f"Computer has {C}, you win")
                user+=1
        elif n=="Scissors":
            if C=="Rock":
                print(f"Computer has {C}, you lose")
                comp+=1
            else:
                print(f"Computer has {C}, you win")
                user+=1
        elif n=="Paper":
            if C=="Scissors":
                print(f"Computer has {C}, you lose")
                comp+=1
            else:
                print(f"Computer has {C}, you win")
                user+=1
    elif n=="0":
        print("Game Over")
        print(f"\nEnd Results:\nYour points: {user} and Computer points: {comp}\n")
        break

    else:
        print("Not valid a choice")