from data import *
from math import *
from random import *

data["general"]["currentState"] = "startScreen"


def playerInput(msg, validation, value):
   while (True):
        insert = input(msg + ": ")
        shouldContinue = False

        if (insert == data["settings"]["StopGame"]["CurrentSetting"]):
            exit()

        if (insert == data["settings"]["MainMenuCommand"]["CurrentSetting"]):
            return "MainMenu"

        if (not insert): return

        for check in validation:
            try:
                insert = value(insert)
            
            except check:
                shouldContinue = True
                print("Wrong input type, please retry")
                break

        if shouldContinue: continue

        return insert


def configGame():
    pass


def initiatePlayer():
    pass 


def selectNumber():
    pass 


def evaluateInput(input):
    pass 


def renderTerminal():
    if (data["general"]["currentState"] == "startScreen"):
        print("""
Hi and welcome to Guess The Number. Please select a section in the menulist, through inputting the given numbers.
If this is your first time playing this game, I strongly advise you to pay a visit to the settings. Menu: 
[1]: Settings,
[2]: StartGame,

        """)

        while (True):
            insert = playerInput("Please, pick a section", [ValueError], int)

            if (insert == "MainMenu"):
                data["general"]["currentState"] = "startScreen"
                return

            if (insert == 1):
                data["general"]["currentState"] = "Settings"
                return

            if (insert == 2):
                return "StartGame"
        

    elif (data["general"]["currentState"] == "Settings"):
        print(f"""
This is the settings, in order to change a setting, please write the setting name (not case sensitive) along with the value. The value outside of the brackets 
is the current setting and the values inside the brackets are possible settings you can change to. Eg: PlayerMode: Multiplayer.
for now click on {data["settings"]["MainMenuCommand"]["CurrentSetting"]} to go back to the start screen. 

PlayerMode: {data["settings"]["PlayerMode"]["CurrentSetting"]} (Multiplayer)
MainMenuCommand: {data["settings"]["MainMenuCommand"]["CurrentSetting"]} (Can be any value. Caution: backwards slash is not allowed, not case sensitive)
StopGame: {data["settings"]["StopGame"]["CurrentSetting"]} (Can be any value. Caution: backwards slash is not allowed, not case sensitive)
MinValue: {data["settings"]["MinValue"]["CurrentSetting"]} (Any intiger 0 and above)
MaxValue: {data["settings"]["MaxValue"]["CurrentSetting"]} (Any intiger 0 and above, if difference between this value and the min value is < 10 this value will be adjusted automatically by the game)
        """)

        insert = playerInput("Please, pick a section", [ValueError], str)

        if (insert == "MainMenu"):
            data["general"]["currentState"] = "startScreen"
            return




def manageGame():
    while (True):
        result = renderTerminal()

        if (result == "StartGame"):
            print("Game is starting")


manageGame()