import random

# Number of rounds
round_num=4

# Function for high-low game
def high_low_game():
    print('Welcome to High-Low Game!')
    
    print('----------------------------------')
    
    # Initializing score
    score = 0
    
    # Game instructions
    for num_round in range(1,round_num + 1):
        print(f'Round{num_round}')

        # Generating random numbers for player and computer
        player_num=random.randint(1,100)

        computer_num= random.randint(1,100)

        # Showing the player's number
        print(f'Your number is {player_num}.')

        # Prompting the user to guess
        while True:
            guess=input("What do you think is your number higher or lower then the computer's number?").lower

            if guess in ['higher','lower']:
                break
            print('Invalid input. Please just enter higher or lower!')

        #Comparing player's and computer's number and checking the guess
        if player_num > computer_num and guess == 'higher':
            print(f"You were absolutely right! The computer's number was {computer_num}.")
            score+=1

        elif player_num < computer_num and guess == 'lower':
            print(f"You were absolutely right! The computer's number was {computer_num}.")
            score+=1

        elif player_num == computer_num:
            print(f"Tough luck! Both numbers are equal. The computer's number was {computer_num}.")

        else:
            print(f"Oho, your number was incorrect, sad. The computer's number was actually {computer_num}.")

        # Displaying the score
        print(f"Now your score is {score}.")

        # Adding a blank line for better visual
        print()

    # Ending with a greeting message
    if score == round_num:
        print("Wow! You did a good job. Well done!")

    elif score >= round_num//2:
        print("You played very well. good job!")

    else:
        print("AOH! Better luck next time. And practice well!")

# Starting the game
high_low_game()