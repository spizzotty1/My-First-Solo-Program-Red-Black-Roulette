# brings in the random module to simulate a roulette wheel spin.

import random
# define user input variable to store player's choice.
player_input = ""

# defines the maximum number of spins to keep in history.
MAX_HISTORY = 5

# stores the results of the past spins in a list.
past_spins = []

# Simulates a spin of a red-black roulette wheel.
def spin():
    return random.choice(["red", "black"])

# main loop that continues until the user decides to quit.
def main():
    print("Hello, and welcome to the roulette game of red and black!")
    print("Let's see how many times in a row you can guess the color correctly.")
    print("You just have to hit r or b to choose red or black and then hit enter.")
    print("If you want to leave the game hit q and enter.")

    win_streak = 0 # Initialize win streak counter
    loss_streak = 0 # Initialize loss streak counter

    while True:
        # prompts the user to spin the wheel or quit.
        player_input = input("R or B (or Q to quit): ").upper().strip()

        if player_input == "Q":
            print("Thanks for playing!")
            break

        if player_input not in ("R", "B"):
            print("Invalid input. Please enter R, B, or Q.")
            continue

        # simulates a spin and stores the result in history.
        result = spin()

        if player_input == "R":
            player_choice = "red"
        else:
            player_choice = "black"

        if player_choice == result:
            print("You Won!")
            win_streak += 1
            loss_streak = 0  # Reset loss streak on a win
            
        else:
            print("Nice try!")
            loss_streak += 1
            win_streak = 0  # Reset win streak on a loss

        past_spins.insert(0, result)
        
        # ensures that the history does not exceed MAX_HISTORY.
        if len(past_spins) > MAX_HISTORY:
            past_spins.pop()
        
        # displays the result of the spin and the history of past spins.
        print(f"The wheel landed on: {result}")
        print(f"Past spins: {past_spins}")
        print(f"Win streak: {win_streak}, Loss streak: {loss_streak}")



if __name__ == "__main__":
    main()

