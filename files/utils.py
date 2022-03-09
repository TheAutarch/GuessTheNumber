

from math import *

dataRoot = {
    "general": {
        "currentState": "startScreen",
    },

    "gameState": "notStarted",

    "invalidSetting": "",

    "currentTurn": 1,

    "randomNumber": 0,

    "winPoints": 100,

    "losePoints": -50,

    "currentPlayer": 1,

    "msg": "",

    "turn": 0,

    "totalTurns": 1,

    "difficulties": [0, 1/2, 1/3, 1/4, 1/5, 1/6],

    "settings": {
        "PlayerMode": {
            "CurrentSetting": "SinglePlayer",
            "Changeable": ["MultiPlayer"],
            "Requirements": ["Only"]
        },

        "MainMenuCommand": {
            "CurrentSetting": "E",
            "Changeable": ["Anything"],
            "Requirements": ["Nothing"]
        },

        "StopGame": {
            "CurrentSetting": "R",
            "Changeable": ["Anything"],
            "Requirements": ["Nothing"]
        },

        "MinValue": {
            "CurrentSetting": 1,
            "Changeable": ["AnyNumber"],
            "Requirements": ["greaterThan", 0]
        },

        "MaxValue": {
            "CurrentSetting": 10,
            "Changeable": ["AnyNumber"],
            "Requirements": ["greaterThan", "MinValue", 9]
        },

        "Difficulty": {
            "CurrentSetting": 2,
            "Changeable": ["AnyNumber"],
            "Requirements": ["between", 1, 5]
        },

    },

    "players": {},

    "numEvaluation": "1",
    "plrEvaluation": "1"
}

def findPlayerFromKey(data, key):
    for i in data["players"]:
        if data["players"][i]["key"] == key: return data["players"][i]


def renderOptions(setting):
    output = ""
    count = 0

    for i in setting: 
        if count > 0: 
            output = output + " " + i
        
        else:
            output = output + i

        count += 1

    return output

    


class Util:
    def __init__(self):
        self.data = dataRoot


    def startScreen(data):
        print("""(Caution: Make sure to remeber commands)
Hi and welcome to Guess The Number. Please select a section in the menulist, through inputting the given numbers.
If this is your first time playing this game, I strongly advise you to pay a visit to the settings. Menu: 
[1]: Settings,
[2]: StartGame,""")

    
    def settings(self, data):
        playerModeOptions = renderOptions(data["settings"]["PlayerMode"]["Changeable"])
        print(f"""
This is the settings, in order to change a setting, please write the setting name (not case sensitive) along with the value. The value outside of the brackets 
is the current setting and the values inside the brackets are possible settings you can change to. Eg: PlayerMode MultiPlayer.
for now click on {data["settings"]["MainMenuCommand"]["CurrentSetting"]} to go back to the start screen. 
PlayerMode: {data["settings"]["PlayerMode"]["CurrentSetting"]} ({playerModeOptions})
MainMenuCommand: {data["settings"]["MainMenuCommand"]["CurrentSetting"]} (Can be any value. Not case sensitive)
StopGame: {data["settings"]["StopGame"]["CurrentSetting"]} (Can be any value. Not case sensitive)
MinValue: {data["settings"]["MinValue"]["CurrentSetting"]} (Any intiger 1 and above)
MaxValue: {data["settings"]["MaxValue"]["CurrentSetting"]} (Any intiger 10 and above, if difference between this value and the min value is < 10 this value will be adjusted automatically by the game)
Difficulty: {data["settings"]["Difficulty"]["CurrentSetting"]} (This setting wil adjust the amount of guesses relative to the intervall. The scale goes from 1-5)
{data["invalidSetting"]}""")


    def game(self, data):
        if (data["gameState"] == "notStarted"):
            return data["settings"]["PlayerMode"]["CurrentSetting"] == "SinglePlayer" and 1 or 2

        elif (data["gameState"] == "started"):
            if (data["turn"] == 0):
                pass

            else:
                pass

            print(data["currentPlayer"])
            currentPlayer = findPlayerFromKey(data, data["currentPlayer"])

            plrState = plrState = f"{currentPlayer['name']}'s points: {currentPlayer['points']}. {currentPlayer['name']}'s wins: {currentPlayer['wins']}. {currentPlayer['name']}'s losses: {currentPlayer['losses']}"

            print(f"""
Game ongoing. Guess a number between {data["settings"]["MinValue"]["CurrentSetting"]} and {data["settings"]["MaxValue"]["CurrentSetting"]}. Current player state: {plrState}.
Current turn: {currentPlayer["name"]}
Attempts left: {floor(data["difficulties"][data["settings"]["Difficulty"]["CurrentSetting"]] * (data["settings"]["MaxValue"]["CurrentSetting"] - data["settings"]["MinValue"]["CurrentSetting"])) - currentPlayer["attempts"]}
""")

            print(data["msg"])

            return "promptTurn"

    def endGameMsg(self, plr, tp, data):
        message = tp == "Win" and "successfully won" or "lost"

        print(f"""
{plr["name"]} {message} this round with {data["turn"]} attempts.""")
        