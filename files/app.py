

from math import *
from random import *
from utils import *
from os import *

dataObject = Util()
print(dataObject.data)

dataObject.data["general"]["currentState"] = "startScreen"


def playerInput(msg, validation, value):
   while (True):
        insert = input(msg + ": ")
        shouldContinue = False

        if (insert == dataObject.data["settings"]["StopGame"]["CurrentSetting"]):
            exit()

        if (insert == dataObject.data["settings"]["MainMenuCommand"]["CurrentSetting"]):
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


def findPlayerFromKey(data, key):
    for i in data["players"]:
        print(data["players"][i])
        if data["players"][i]["key"] == key: return i


def renderTerminal():
    system("cls")

    if (dataObject.data["general"]["currentState"] == "startScreen"):
        dataObject.startScreen()

        insert = playerInput("Please write a command", [ValueError], int)

        if (insert == "MainMenu"):
            dataObject.data["general"]["currentState"] = "startScreen"
            return

        if (insert == 1):
            dataObject.data["general"]["currentState"] = "Settings"
            return

        if (insert == 2):
            dataObject.data["general"]["currentState"] = "game"
            return "StartGame"

    elif (dataObject.data["general"]["currentState"] == "Settings"):
        dataObject.settings(dataObject.data)

        insert = playerInput("Please write a command", [ValueError], int)

        if (insert == "MainMenu"):
            dataObject.data["general"]["currentState"] = "startScreen"
            return

    elif (dataObject.data["general"]["currentState"] == "game"):

        result = dataObject.game(dataObject.data)

        if (result == "initPlr1"):
            name = playerInput("Enter your name", [ValueError], str)

            dataObject.data["currentPlayer"] = 1

            dataObject.data["players"]["player1"] = {
                "name": name,
                "points": 0,
                "key": 1
            }

            dataObject.data["gameState"] = "started"

        elif (result == "initPlr1And2"):
            name1 = playerInput("Player 1: Enter your name: ", [ValueError], str)
            name2 = playerInput("Player 2: Enter your name: ", [ValueError], str)

            dataObject.data["currentPlayer"] = 1

            dataObject.data["players"]["player1"] = {
                "name": name1,
                "points": 0,
                "key": 1
            }

            dataObject.data["players"]["player2"] = {
                "name": name2,
                "points": 0,
                "key": -1
            }

            #dataObject.data["randomNumber"]: Enter number

            dataObject.data["gameState"] = "started"

        elif (result == "promptTurn"):
            number = playerInput("Guess number", [ValueError], str)

            evaluateInput(number)



def manageGame():
    while (True):
        result = renderTerminal()

        if (result == "StartGame"):
            print("Game is starting")


manageGame()
