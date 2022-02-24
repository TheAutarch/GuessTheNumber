

dataRoot = {
    "general": {
        "currentState": "startScreen",
    },

    "gameState": "notStarted",

    "currentTurn": 1,

    "randomNumber": 0,

    "settings": {
        "PlayerMode": {
            "CurrentSetting": "SinglePlayer",
        },

        "MainMenuCommand": {
            "CurrentSetting": "E",
        },

        "StopGame": {
            "CurrentSetting": "R",
        },

        "MinValue": {
            "CurrentSetting": 1,
        },

        "MaxValue": {
            "CurrentSetting": 10,
        },

    },

    "players": {},

    "numEvaluation": "1",
    "plrEvaluation": "1"
}

def findPlayerFromKey(data, key):
    for i in data["players"]:
        if data["players"][i]["key"] == key: return data["players"][i]


class Util:
    def __init__(self):
        self.data = dataRoot


    def startScreen(data):
        print("""
(Caution: The game is not optimized for other operating systems than windows atm)
Hi and welcome to Guess The Number. Please select a section in the menulist, through inputting the given numbers.
If this is your first time playing this game, I strongly advise you to pay a visit to the settings. Menu: 

[1]: Settings,
[2]: StartGame,
""")

    
    def settings(self, data):
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


    def game(self, data):
        if (data["gameState"] == "notStarted"):
            if (data["settings"]["PlayerMode"]["CurrentSetting"] == "SinglePlayer"):
                return "initPlr1"

            else:
                return "initPlr1and2"

        elif (data["gameState"] == "started"):
            plrState = ""
            
            if (data["settings"]["PlayerMode"]["CurrentSetting"] == "SinglePlayer"):
                plrState = f"{data['players']['player1']['name']}'s points: {data['players']['player1']['points']}"

            currentPlayer = findPlayerFromKey(data, data["currentPlayer"])


            print(f"""
Game ongoing. Guess a number between {data["settings"]["MinValue"]["CurrentSetting"]} and {data["settings"]["MaxValue"]["CurrentSetting"]}. Current player state: {plrState}.
Current turn: {currentPlayer["name"]}
""")

            return "promptTurn"
        