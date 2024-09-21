
import random

print("*"*20,end=" ")
print("WELCOME TO GUESS THE NUMBER",end=" ")
print("*"*20)
print()
print("*"*5," INSTRUCTIONS ","*"*5)
print("1.You have to guess a number between 1 to 25.")
print("2.You will be given 5 attempts to guess the number.")
print("3.If you are able to guess the number within 5 attempts,you will win else you will lose!!")
print("4.There will be some hints given to you :-")
print("Hints:-")
print("If the guess number is higher than the actual = \"HIGH\" will be printed.")
print("If the guess number is lower than the actual = \"LOW\" will be printed.")
print()
n = random.randint(1,25)
found=-1

for i in range(1,6):
    print("Attempt",i)
    a= int(input("Enter a number between 1 to 25:- "))
    print()
    if(a<0 or a>25):
        print("Invalid Input")
        found=0
        break
    if(a==n):
        print("You guessed the number !! You won !!")
        found=1
        break
    elif(a>n):
        print("HIGH")
        print()
    else:
        print("LOW")
        print()
        
    
if(found==-1):
    print("You Lost, the number was",n,"!!!")
    
print()
print("*"*20,end=" ")
print("THANKYOU FOR PLAYING, BYE !!",end=" ")
print("*"*20)
