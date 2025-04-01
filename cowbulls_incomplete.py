import random

def compare_numbers(number, user_guess):
    cows = 0
    bulls = 0
    
    for i in range(4):
        if user_guess[i] == number[i]:  
            bulls += 1
        elif user_guess[i] in number:  
            cows += 1
    
    return cows, bulls  

playing = True
number = str(random.randint(1000, 9999))  
guesses = 0
print(number)  

print("Let's play a game of Cowbull!")
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in the wrong place, you get a cow.")
print("For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type 'exit' at any prompt to exit.")

while playing:
    user_guess = input("Give me your best 4-digit guess: ")
    
    if user_guess.lower() == "exit":
        break
    
    if not user_guess.isdigit() or len(user_guess) != 4:  
        print("Please enter a valid 4-digit number.")
        continue
    
    cowbullcount = compare_numbers(number, user_guess)
    guesses += 1

    print(f"You have {cowbullcount[0]} cows and {cowbullcount[1]} bulls.")

    if cowbullcount[1] == 4:  
        playing = False
        print(f"You win the game after {guesses} guesses! The number was {number}.")
        break
    else:
        print("Your guess isn't quite right, try again.")
