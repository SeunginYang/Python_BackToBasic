
# 1. random.randit(a,b) Return a random interger N such that a<= N <= b. 
from random import randint

print("Welcome to Python Casino")
pc_choice = randint(1,50)


playing = True

while playing:
    user_choice = int(input("Choose your number (1-50)"))
    if user_choice== pc_choice:
        print("You won!")
        playing = False
    elif user_choice > pc_choice:
        print("You need to choose Lower number!")
    elif user_choice < pc_choice:
        print("You need to choose Higher number!")                  





