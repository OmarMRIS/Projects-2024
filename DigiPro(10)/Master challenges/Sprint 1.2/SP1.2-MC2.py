import random

Times_Rolled = 0

while True: # Prompt
    print('I got a dice, should I roll it or nah? (1/2):\n')
    print("1. Yeah, do it.")
    print("2. Nah.")

    User_Reply = int(input())

    if User_Reply == 1: # Randomizer
        print("Okay dokey")
        Times_Rolled += 1
        Roll = random.randint(1, 6)
        print("Ight man you have rolled", Roll)

    elif User_Reply == 2:
        print("Ight man Off you go then")
        break  # Exit the loop if the user chooses not to play again

    else:
        print("Bro what are you doing? I told you to put 1 or 2")

    print("So you wanna play again? (1/2)") # continuation 
    print("1. Yeah, I love it!")
    print("2. Nah")
    
    play_again = int(input())

    if play_again == 2:
        print("Thanks for playing dude!!.")
        print(f"You have rolled the dice a total of {Times_Rolled} time(s)")
        break  # Exit the loop if the user chooses not to play again
