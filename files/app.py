from decimal import DivisionByZero
from data import *
from math import *
from random import *


def playerInput(msg, validation, value):
   while (True):
        insert = input(msg)
        shouldContinue = False

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


def evaluateInput():
    pass 


def manageRounds():
    pass


