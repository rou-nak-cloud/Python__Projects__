import random

def welcome_message():
    print("""
    Welcome to the PIG game! A game where you try to reach 50 points before your opponents.
    On your turn, you can either 'roll' or 'hold'.
    If you 'roll' and get a 1, you score no points that turn and your turn ends.
    If you 'roll' and get 2-10, that number is added to your turn total and you can choose to 'roll' again or 'hold'.
    If you 'hold', your turn total is added to your overall score and your turn ends and if you get 1 then all scores will be lost.
    First player to reach 50 points wins!
    """)
welcome_message()


def roll_dice():
    min_value = 1
    max_value = 10
    roll = random.randint(min_value, max_value)
    return roll


#finding players
while True:
    players = input("Enter number of players to play (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("Please enter a number between 2 and 4.")
            
print(players)

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        current_score = 0
        print(f"\nPlayer {player_idx + 1}'s turn. Current overall score: {player_scores[player_idx]}\n")
        
        while True:
            should_roll = input("Do you want to 'roll(r)'? ")
            if should_roll.lower() != 'r' and should_roll.lower() != 'h':
                print("Invalid input. Please enter 'r' to roll or 'h' to hold.")
                break
            
            value = roll_dice()
            if value == 1:
                print("You rolled a 1! No points this turn.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}!")
                
            print(f"Your current turn score is {current_score}.")
            
            should_hold = input("Do you want to 'hold(h)' or 'not(n)'? ")
            if should_hold.lower() == 'h':
                player_scores[player_idx] += current_score
                print(f"You held! Your overall score is now {player_scores[player_idx]}.")
                break
            elif should_hold.lower() == 'n':
                continue
            else:
                print("Invalid input. Please enter 'h' to hold or 'n' to continue rolling next time.")
                break
            
            
max_score_player = max(player_scores)
winning_idx = player_scores.index(max_score_player)
print(f"\nPlayer {winning_idx + 1} wins with a score of {max_score_player} towards the winning {max_score} points! Congratulations!")