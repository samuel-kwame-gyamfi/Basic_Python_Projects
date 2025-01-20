import random

number_to_Guess = random.randint(1, 100)

while True:
    try:
        user = int(input("Guess the number (between 1 to 100): "))
        
        if user > number_to_Guess:
            print("Too high!")
        elif user < number_to_Guess:
            print("Too low!")
        elif user == number_to_Guess:
            print("Congratulations, you guessed it right!")
            break
    except ValueError:
        print("Please enter a valid number.")



