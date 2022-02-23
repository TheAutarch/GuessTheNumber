from data import *
from math import *
from random import *
from os import *

dataObject = data()

dataObject["general"]["currentState"] = "startScreen"


def playerInput(msg, validation, value):
   while (True):
        insert = input(msg + ": ")
        shouldContinue = False

        if (insert == dataObject["settings"]["StopGame"]["CurrentSetting"]):
            exit()

        if (insert == dataObject["settings"]["MainMenuCommand"]["CurrentSetting"]):
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
    system("cls")

    print(dataObject["text"][dataObject["general"]["currentState"]])

    if (dataObject["general"]["currentState"] == "startScreen"):
        insert = playerInput("Please write a command", [ValueError], int)

        if (insert == "MainMenu"):
            dataObject["general"]["currentState"] = "startScreen"
            return

        if (insert == 1):
            dataObject["general"]["currentState"] = "Settings"
            return

        if (insert == 2):
            dataObject["general"]["currentState"] = "game"
            return "StartGame"
        
    elif (dataObject["general"]["currentState"] == "Settings"):
        insert = playerInput("Please write a command", [ValueError], int)

        if (insert == "MainMenu"):
            dataObject["general"]["currentState"] = "startScreen"
            return

    elif (dataObject["general"]["currentState"] == "game"):
        insert = playerInput("Please write a command", [ValueError], int)

        if (insert == "MainMenu"):
            dataObject["general"]["currentState"] = "startScreen"
            return



def manageGame():
    while (True):
        result = renderTerminal()

        if (result == "StartGame"):
            print("Game is starting")


manageGame()