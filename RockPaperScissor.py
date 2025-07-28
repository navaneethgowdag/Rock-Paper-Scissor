import random

def rps():
    print("WELCOME TO THE GAME.....")
    name = input("Enter Your Name: ").title()
    print("You Are Playing ROCK PAPER SCISSORS")
    print(f"{name} vs Computer")
    
    choices = ["rock", "paper", "scissor"]
    you = 0
    computer_score = 0

    while you < 3 and computer_score < 3:
        player = input("Rock, Paper, Scissor: ").lower()
        if player not in choices:
            print("ENTER VALID OPTION!!!")
            continue

        computer = random.choice(choices)
        print(f"Computer: {computer}")
        print(f"Player: {player}")

        if player == computer:
            print("It's a tie round! Both get a point.")
            you += 1
            computer_score += 1
        elif (
            (player == "rock" and computer == "scissor") or
            (player == "paper" and computer == "rock") or
            (player == "scissor" and computer == "paper")
        ):
            print("You win this round!")
            you += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"SCORE = {name}: {you}, Computer: {computer_score}\n")

    print("GAME ENDS!!")
    print(f"FINAL SCORE = {name}: {you}, Computer: {computer_score}")

    if you == 3 and computer_score < 3:
        print("CONGRATS!! YOU WON :)")
    elif computer_score == 3 and you < 3:
        print("COMPUTER WON!! BETTER LUCK NEXT TIME")
    else:
        print("MATCH IS A TIE!!")

# Main game loop
def main():
    while True:
        rps()
        play_again = input("DO YOU WANT TO PLAY AGAIN? (YES or NO): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("THANK YOU, SEE YOU :)")
            print("------------------------------------")
            break

if __name__ == "__main__":
    main()
