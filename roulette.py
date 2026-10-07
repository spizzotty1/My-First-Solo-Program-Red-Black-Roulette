# brings in the random module to simulate a roulette wheel spin.

import random

# Simulates a spin of a red-black roulette wheel.

def spin():
    return random.choice(["red", "black"])

# this print statement calls the spin function and prints the result of the spin to the console.

print(spin())

