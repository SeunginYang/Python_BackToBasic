# user_choice = int(input("Choose your number."))

# pc_choice = 50

# if user_choice== pc_choice:
#     print("You won!")
# elif user_choice > pc_choice:
#     print("You need to choose Lower number")
# elif user_choice < pc_choice:
#     print("You need to choose Higher number")

#1. random.randit(a,b) Return a random interger N such that a<= N <= b. 
# from random import randint

# user_choice = int(input("Choose your number."))

# pc_choice = randint(1,50)

# if user_choice== pc_choice:
#     print("You won!")
# elif user_choice > pc_choice:
#     print("You need to choose Lower number! Computer chose", pc_choice)
# elif user_choice < pc_choice:
#     print("You need to choose Higher number! Computer chose", pc_choice)

distance = 0

while distance <20:
    print("I'm running:", distance, "km")
    distance += 1

dishes = 0

while dishes < 100:
    print("When i go to Sushi buffet,",dishes,"are my limits")
    dishes += 5
