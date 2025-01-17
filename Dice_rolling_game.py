import random
count = 0
while True:
    choice = input("Roll the dice? (Yes/NO) :")
    if choice == "Yes":
        count+=1
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"{dice1}, {dice2}")
        print(f" Number of dice rolled {count}")
    elif choice == "No":
        print("Thanks for playing the game")
        print(f" Number of dice rolled {count}")
        break
    else:
        print("Invalid choice")
     

