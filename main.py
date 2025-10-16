import random
comp = random.choice([1, 2, 3])

you_dict={"r":1, "p":2, "s":3}
rev_dict={1:"Rock", 2:"Paper", 3:"Scissors"}

you_str=input("Enter your choice (r/p/s): ")
you=you_dict[you_str]

print(f"you chose : {rev_dict[you]} \n computer chose : {rev_dict[comp]}")

if(you == comp):
    print("It's a tie!")
else:
    if((you==1 and comp==3) or (you==2 and comp==1) or (you==3 and comp==2)):
        print("You win!")
    elif((comp==1 and you==3) or (comp==2 and you==1) or (comp==3 and you==2)):
        print("you lose!")
    else:
        print("Something went wrong!")

