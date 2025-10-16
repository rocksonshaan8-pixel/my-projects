import random
c=random.randint(1,100)
u=-1
a=0
while(u!=c):
    a+=1
    u=int(input("Guess the number between 1 to 100: "))
    if(u>c):
        print("Lower number please")
    elif(u<c):
        print("Higher number please")
print(f"You guessed it right and the number is {c}")
print(f"Number of attempts: {a}")
