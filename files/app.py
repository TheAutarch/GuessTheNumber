from math import *
from random import *
from utils import *

dataObject = Util()

dataObject.data["general"]["currentState"] = "startScreen"


def clearPlayerState(gameState):
    dataObject.data["general"]["currentState"] = "game"
    dataObject.data["gameState"] = gameState 
    dataObject.data["currentTurn"] = 1
    dataObject.data["msg"] = ""
    dataObject.data["turn"] = 0
    dataObject.data["randomNumber"] = randint(dataObject.data["settings"]["MinValue"]["CurrentSetting"], dataObject.data["settings"]["MaxValue"]["CurrentSetting"])

    for i in dataObject.data["players"]:
        plr = dataObject.data["players"][i]
        plr["attempts"] = 0

def clearConsole():
    print("\n" * 150)


def findSetting(key):
    for i in dataObject.data["settings"]:
        if (key.lower() == i.lower()):
            return dataObject.data["settings"][i]


def createPlayerData(name, key):
    return {
            "name": name,
            "points": 0,
            "key": key,
            "guess": 0,
            "wins": 0,
            "losses": 0,
            "attempts": 0,
            }


def displayResults():
    currentPlayer = findPlayerFromKey(dataObject.data, dataObject.data["currentPlayer"])

    components = [
        f"Enter the main menu command, if you'd like to access the main menu and change settings. (Caution: entering the main menu will restart game state). Cmd: {dataObject.data['settings']['MainMenuCommand']['CurrentSetting']}",
        f"Enter the shutdown command, if you'd like to end your game session. Cmd: {dataObject.data['settings']['StopGame']['CurrentSetting']}",
    ]

    playerWins = "Amount of wins: "
    playerLosses = "Amount of losses: "
    playerPoints = "Amount of points: "
    
    for i in dataObject.data["players"]:
        plr = dataObject.data["players"][i]

        playerWins += plr["name"] + ": " + str(plr["wins"]) + "  "
        playerLosses += plr["name"] + ": " + str(plr["losses"]) + "  "
        playerPoints += plr["name"] + ": " + str(plr["points"]) + "  "

    return f"""{components[0]}
{components[1]}
{playerWins}
{playerLosses}
{playerPoints}
Any other input, but core commands will commence a new round.
"""


def initPlayers(loops):
    keys = [1, -1]

    for i in range(1, loops + 1):
        name = playerInput(f"Player{i}: Enter your name", [ValueError], str)

        if (name == "MainMenu"):
            clearPlayerState("notStarted")
            dataObject.data["general"]["currentState"] = "startScreen"
            return "MainMenu"


        dataObject.data["players"]["player" + str(i)] = createPlayerData(name, keys[0])
        keys.remove(keys[0])


def validateSetting(key, value, current):
    setting = findSetting(key)
    count = 0

    for i in setting["Changeable"]:
        if (i == "Anything"):
            return value

        if (i == "AnyNumber"):
            passed = True

            try: 
                value = int(value)

            except ValueError:
                print("You can only assign integers to this setting")
                passed = False

            if (passed):
                if (setting["Requirements"][0] == "greaterThan"):
                    if (type(setting["Requirements"][1])) == int:
                        if (int(value) <= setting["Requirements"][1]):
                            value = int(setting["Requirements"][1])

                        if (int(value) > dataObject.data["settings"]["MaxValue"]["CurrentSetting"] - 9):
                            value = dataObject.data["settings"]["MaxValue"]["CurrentSetting"] - 9

                    else:
                        if (int(value) < dataObject.data["settings"][setting["Requirements"][1]]["CurrentSetting"] + setting["Requirements"][2]):
                            value = dataObject.data["settings"][setting["Requirements"][1]]["CurrentSetting"] + setting["Requirements"][2]

                elif (setting["Requirements"][0] == "between"):
                    if (setting["Requirements"][1] > int(value)):
                        value = setting["Requirements"][1]

                    elif (int(value) > setting["Requirements"][2] ):
                        value = setting["Requirements"][2]

                    else:
                        value = value

                return int(value)

        if (i.lower() == value.lower()):
            setting["Changeable"].remove(i)
            setting["Changeable"].append(current)
            return i

        count += 1


def playerInput(msg, validation, value):
   while (True):
        insert = input(msg + ": ")
        shouldContinue = False

        if ((str(insert)).lower() == dataObject.data["settings"]["StopGame"]["CurrentSetting"].lower()):
            exit()

        if ((str(insert)).lower() == dataObject.data["settings"]["MainMenuCommand"]["CurrentSetting"].lower()):
            return "MainMenu"

        if (dataObject.data["general"]["currentState"] == "Win" or dataObject.data["general"]["currentState"] == "Lose"):
            return "newGame"

        if (dataObject.data["general"]["currentState"] == "Settings"):
            cmd = insert.split(" ")
            cmdContinue = False

            for i in dataObject.data["settings"]:
                if (str(i).lower() == cmd[0].lower()):
                    if (len(cmd) == 2):
                        setting = findSetting(cmd[0])

                        val = validateSetting(cmd[0], cmd[1], setting["CurrentSetting"])

                        if (val):
                            setting["CurrentSetting"] = val
                            cmdContinue = True
                            clearConsole()
                            dataObject.settings(dataObject.data)

            if (cmdContinue): return


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


def evaluateInput(input):
    currentPlayer = findPlayerFromKey(dataObject.data, dataObject.data["currentPlayer"])

    num = dataObject.data["randomNumber"]  

    if (input > num):
        if (floor(dataObject.data["difficulties"][dataObject.data["settings"]["Difficulty"]["CurrentSetting"]] * (dataObject.data["settings"]["MaxValue"]["CurrentSetting"] - dataObject.data["settings"]["MinValue"]["CurrentSetting"])) - currentPlayer["attempts"] == 0):
            return "Lose"
        
        return "The number you have entered is greater than the hidden number. Try a lower number"

    elif (input < num):
        if (floor(dataObject.data["difficulties"][dataObject.data["settings"]["Difficulty"]["CurrentSetting"]] * (dataObject.data["settings"]["MaxValue"]["CurrentSetting"] - dataObject.data["settings"]["MinValue"]["CurrentSetting"])) - currentPlayer["attempts"] == 0):
            return "Lose"

        return "The number you have entered is lower than the hidden number. Try a greater number"

    return "Win"

def findPlayerFromKey(data, key):
    for i in data["players"]:
        if data["players"][i]["key"] == key: return data["players"][i]


def renderTerminal():
    clearConsole()

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

        insert = playerInput("Please write a command", [ValueError], str)

        if (insert == "MainMenu"):
            dataObject.data["general"]["currentState"] = "startScreen"
            return

    elif (dataObject.data["general"]["currentState"] == "game"):
        result = dataObject.game(dataObject.data)

        if (type(result) == int): 
            respone = initPlayers(result)
            if (respone == "MainMenu"): return

            dataObject.data["currentPlayer"] = 1
            dataObject.data["randomNumber"] = randint(dataObject.data["settings"]["MinValue"]["CurrentSetting"], dataObject.data["settings"]["MaxValue"]["CurrentSetting"])
            dataObject.data["gameState"] = "started"

        if (result == "promptTurn"):
            currentPlayer = findPlayerFromKey(dataObject.data, dataObject.data["currentPlayer"])
            number = playerInput("Guess number", [ValueError], int)

            if (number == "MainMenu"):
                clearPlayerState("notStarted")
                dataObject.data["general"]["currentState"] = "startScreen"
                return

            currentPlayer["attempts"] += 1

            if (dataObject.data["settings"]["PlayerMode"]["CurrentSetting"] == "MultiPlayer"):
                dataObject.data["currentPlayer"] *= -1
                
            dataObject.data["msg"] = evaluateInput(number)

            if (dataObject.data["msg"] == "Win"):
                dataObject.data["general"]["currentState"] = "Win"

            elif (dataObject.data["msg"] == "Lose"):
                dataObject.data["general"]["currentState"] = "Lose"
                
    elif (dataObject.data["general"]["currentState"] == "Win"):
        currentPlayer = findPlayerFromKey(dataObject.data, dataObject.data["currentPlayer"] * -1)

        dataObject.endGameMsg(currentPlayer, "Win", dataObject.data)

        currentPlayer["wins"] += 1
        currentPlayer["points"] += dataObject.data["winPoints"]

        otherPlayer = findPlayerFromKey(dataObject.data, dataObject.data["currentPlayer"])
        otherPlayer["losses"] += 1
        otherPlayer["points"] += dataObject.data["losePoints"]

        if (otherPlayer["points"] < 0):
            otherPlayer["points"] = 0

        results = displayResults()

        insert = playerInput(results, [ValueError], str)

        if (insert == "MainMenu"):
            clearPlayerState("notStarted")
            dataObject.data["general"]["currentState"] = "startScreen"
            return


        if (insert == "newGame"):
            clearPlayerState("started")

    elif (dataObject.data["general"]["currentState"] == "Lose"):
        currentPlayer = findPlayerFromKey(dataObject.data, dataObject.data["currentPlayer"])

        dataObject.endGameMsg(currentPlayer, "Lose", dataObject.data)

        for i in dataObject.data["players"]:
            plr = dataObject.data["players"][i]

            plr["losses"] += 1
            plr["points"] += dataObject.data["losePoints"]

            if (plr["points"] < 0):
                plr["points"] = 0

        results = displayResults()

        insert = playerInput(results, [ValueError], str)

        if (insert == "MainMenu"):
            clearPlayerState("notStarted")
            dataObject.data["general"]["currentState"] = "startScreen"
            return

        if (insert == "newGame"):
            clearPlayerState("started")



def manageGame():
    while (True):
        renderTerminal()


manageGame()