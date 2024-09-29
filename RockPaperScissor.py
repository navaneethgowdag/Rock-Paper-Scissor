import random

def rps():
    print('WELL COME TO THE GAME.....')
    name = input('Enter Your Name: ').title()
    print('You Are Playing ROCK PAPER SCISSOR')
    print(f'{name} vs Computer')
    choices = ["rock", "paper", "scissor"]

    you = 0
    system = 0

    while True:
        if you == 3 or system == 3:
            break

        player = input('Rock,Paper,Scissor: ').lower()
        computer =random.choice(choices)

        if computer == player:
            print('Computer:', computer)
            print('Player: ', player)
            you += 1
            system += 1
        elif player == 'rock':
            if computer == 'paper':
                print('Computer:', computer)
                print('Player: ', player)
                system += 1
            if computer == 'scissor':
                print('Computer:', computer)
                print('Player: ', player)
                you += 1
        elif player == 'paper':
            if computer == 'rock':
                print('Computer:', computer)
                print('Player: ', player)
                you += 1
            if computer == 'scissor':
                print('Computer:', computer)
                print('Player: ', player)
                system += 1
        elif player == 'scissor':
            if computer == 'rock':
                print('Computer:', computer)
                print('Player: ', player)
                system += 1
            if computer == 'paper':
                print('Computer:', computer)
                print('Player: ', player)
                you += 1
        elif computer != player:
            print('ENTER VALID OPTION!!!')
        print(f'SCORE = {name} :{you},Computer:{system}')

    print('GAME ENDS!!')
    print(f'FINAL SCORE = {name} :{you},Computer:{system}')

    if you == 3 and system < 3:
        return 'CONGRATS!! , YOU WON:)'
    elif system == 3 and you < 3:
        return 'COMPUTER WON!!, BETTER LUCK NEXT TIME'
    elif you == 3 and system == 3:
        return "MATCH IS TIE!!"


rps()


for loop in iter(int, 1):
    print('DO YOU WANT TO PLAY AGAIN !!')
    game = input('YES or NO: ').lower()
    if 'yes' in game:
        print(rps())
    elif 'no' in game:
        break
    elif 'yes' or 'no' not in game:
        print('ENTER VALID INPUT!!')

print(f'THANK YOU , SEE YOU:)')
print("------------------------------------")
