from random import randint

def generator():
    return randint(1, 10)

def guess():
    number_to_guess = generator()
    guess_left = 3
    flag = 0
    
    while guess_left > 0:
        user_guess = int(input("Put a number: "))
        
        if user_guess == number_to_guess:
            flag = 1
            break
        else:
            print("Wrong Guess!!")
        
        guess_left -= 1
    
    if flag == 1:
        return True
    else:
        return False

print("Welcome to the Lucky Draw Game.")
player_name = input("Enter your name: ")
print("Hello, " + player_name + "!")
start_game = input("Shall we start the game? (Y/N): ")

while True:
    if start_game.upper() == "Y":
        print("Ok!! The game is starting...")
        if guess():
            print("Congratulations!! You won.")
        else:
            print("Better luck next time.")
        break
    elif start_game.upper() == "N":
        print("Goodbye!")
        break
    else:
        start_game = input("Invalid input. Shall we start the game? (Y/N): ")
  
                