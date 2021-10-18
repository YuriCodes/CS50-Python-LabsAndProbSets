from cs50 import get_float

# Get input from user

change = get_float("Change: ")

# Keep prompting if amount is less than 0

while change <= 0:
    change = get_float("Change: ")

# Set a counter for coins and set cents value

coins = 0
cents = round(change * 100)

# Evaluate cents to return right amount of coins 

while cents > 0:
    if cents >= 25:
        cents = cents - 25
        coins = coins + 1
    elif cents >= 10:
        cents = cents - 10
        coins = coins + 1
    elif cents >= 5:
        cents = cents - 5
        coins = coins + 1
    elif cents >= 1:
        cents = cents - 1
        coins = coins + 1

print(coins)



