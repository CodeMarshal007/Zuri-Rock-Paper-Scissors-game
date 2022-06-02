import random

#A ROCK-PAPER-SCISSORS GAME

print("welcome to rock-paper-scissors")

possible_options = ["R", "P", "S"]

game_running = True
while game_running:
    #checking if player entered a valid option
    is_valid = True
    while is_valid:
        player_option = input("Enter your option, you have the options of 'R' for Rock, 'P' for Paper, or 'S' for Scissors: ").upper()

        if player_option in possible_options:
            is_valid = False
        else:
            print("Error: you entered an invalid option, try again")
            continue

    CPU_option = random.choice(possible_options)

    if player_option == CPU_option:
            print(f"Player ({player_option}): CPU ({CPU_option})")
            print("It is a tie. Try again")

    elif player_option == "S" and CPU_option == "P":
            print("Player (Scissors): CPU (Paper)")
            print("The winner is Player!!!")
            break

    elif player_option == "P" and CPU_option == "R":
            print("Player (Paper): CPU (Rock)")
            print("The winner is Player!!!")
            break

    elif player_option == "R" and CPU_option == "S":
            print("Player (Rock): CPU (Scissors)")
            print("The winner is Player!!!")
            break

    elif CPU_option == "S" and player_option == "P":
        print("Player (Paper): CPU (Scissors)")
        print("The winner is CPU!!!")
        break

    elif CPU_option == "P" and player_option == "R":
        print("Player (Rock): CPU (Paper)")
        print("The winner is CPU!!!")
        break

    elif CPU_option == "R" and player_option == "S":
        print("Player (Scissors): CPU (Rock)")
        print("The winner is CPU!!!")
        break