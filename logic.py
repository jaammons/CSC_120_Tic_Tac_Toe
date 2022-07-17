gameboard = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
player = "X"
gameCurrent = True
win = None

print("Hello Players, This is Tic Tac Toe! Good Luck")
def printticboard(gameboard):
    print(gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2])
    print("")
    print(gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5])
    print("")
    print(gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8])

def selectaplayer(gameboard):
    select = int(input("Select a number 0-8: "))
    if select >= 0 and select < 9 and gameboard[select] == "-":
        gameboard[select] = player
    else:
        print("A player has already chose that spot! Try again!")

def checkup(gameboard):
    global win
    if gameboard[0] == gameboard [1] == gameboard[2] and gameboard[0] != "-":
        win = gameboard[0]
        return True
    elif gameboard[3] == gameboard [4] == gameboard[5] and gameboard[3] != "-":
        win = gameboard[3]
        return True
    elif gameboard[6] == gameboard [7] == gameboard[8] and gameboard[6] != "-":
        win = gameboard[6]
        return True

def checkdown(gameboard):
    global win
    if gameboard[0] == gameboard [3] == gameboard[6] and gameboard[0] != "-":
        win = gameboard[0]
        return True
    elif gameboard[1] == gameboard [4] == gameboard[7] and gameboard[1] != "-":
        win = gameboard[1]
        return True
    elif gameboard[2] == gameboard [5] == gameboard[8] and gameboard[2] != "-":
        win = gameboard[2]
        return True

def checkcross(gameboard):
    global win
    if gameboard[0] == gameboard [4] == gameboard[8] and gameboard[0] != "-":
        win = gameboard[0]
        return True
    elif gameboard[2] == gameboard [4] == gameboard[6] and gameboard[2] != "-":
        win = gameboard[2]
        return True

def checkTie(gameboard):
    global gameCurrent
    if "-" not in gameboard:
        print("It is a tie! Please play again to settle the tie!")
        gameCurrent = False

def checkWinnerWinner():
    global gameCurrent
    if checkcross(gameboard) or checkup(gameboard) or checkdown(gameboard):
        print(f"The winner is {win}")
        gameCurrent = False

def playerswitching(gameboard):
    global player
    if player == "X":
        player = "0"
    else:
        player = "X"

while gameCurrent:
    printticboard(gameboard)
    selectaplayer(gameboard)
    checkWinnerWinner()
    checkTie(gameboard)
    playerswitching(gameboard)

