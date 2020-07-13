from random import choice
a="Welcome to snake water gun game.\nYou will get 5 chances to play with computer. Player to win the most games in 5 games will be the winner.\n"
print(a.upper())

def game():
    option=("snake","water","gun")
    totalgame=5
    counter=1
    userwinnum=0
    botwinnum=0
    gamedraw=0

    for i in range(1,totalgame+1):
        bot = choice(option)
        print(bot)
        print("What do you want to select?")
        d={1:"snake",2:"water",3:"gun"}
        user=int(input("1:Snake 2:Water 3:Gun ->"))
        userinput=d.get(user)
        if userinput==bot:
            print(f"Game draw. Player and bot have selected option {bot}.\n ")
            gamedraw += 1
            counter+=1
        elif userinput == 1:
            if bot=="water":
                print(bot)
                print(f"Player won as Player selected {userinput} and bot selected {bot}.\n")
                userwinnum+=1
                counter+=1
            else:
                print(bot)
                print(f"Bot won as Player selected {userinput} and bot selected {bot}.\n ")
                botwinnum += 1
                counter += 1
        elif userinput ==2:
            if bot =="snake":
                print(f"bot won as Player selected {userinput} and bot selected {bot}.\n")
                botwinnum+=1
                counter+=1
            else:
                print(f"Player won as Player selected {userinput} and bot selected {bot}.\n")
                userwinnum+=1
                counter+=1
        else:
            if bot=="snake":
                print(f"player won as Player selected {userinput} and bot selected {bot}.\n")
                userwinnum+=1
                counter+=1
            else:

                print(f"Bot won as Player selected {userinput} and bot selected {bot}.\n")
                botwinnum+=1
                counter+=1

    if counter >5:
        print("Game over")
        print(f'User has won {userwinnum} times.\nComputer has won {botwinnum} times.\nGame draw ={gamedraw}.\n')

    if userwinnum < botwinnum:
        print("Compputer has won more games than you. That's why, the overall winner is the computer.")
    elif userwinnum > botwinnum:
        print("Congratulation!!! You have won overall game.")
    else:
        print("Game is draw!!!!")

game()


