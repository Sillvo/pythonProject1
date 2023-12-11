import random

# Initialize the game board
board = ['_' for _ in range(10)]

# The player places their ship
player_ship = int(input("Enter the position of your ship (0-9): "))
board[player_ship] = 'P'

# The bot places its ship
bot_ship = random.randint(0, 9)
while bot_ship == player_ship:
    bot_ship = random.randint(0, 9)
board[bot_ship] = 'B'

# The game loop
while True:
    # The player takes their turn
    player_guess = int(input("Enter your guess (0-9): "))
    if player_guess == bot_ship:
        print("You hit the bot's ship!")
        break
    else:
        print("You missed!")

    # The bot takes its turn
    bot_guess = random.randint(0, 9)
    if bot_guess == player_ship:
        print("The bot hit your ship!")
        break
    else:
        print("The bot missed!")

print("Game over!")