gameboard = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
player = "X"
gameActive = True
win = None

print("Hello User, here is the game board you will be playing on today! As alwasy good luck and have fun")
def printboard(gameboard):
    print(gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2])
    print("")
    print(gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5])
    print("")
    print(gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8])

def playerselect(gameboard):
    select = int(input("Select a number 0-8: "))
    if select >= 0 and select < 9 and gameboard[select] == "-":
        gameboard[select] = player
    else:
        print("Oops player is already in that spot!")

def checkrow(gameboard):
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

def checkcol(gameboard):
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
    global gameActive
    if "-" not in gameboard:
        print("It is a tie!")
        gameActive = False

def checkWin():
    global gameActive
    if checkcross(gameboard) or checkrow(gameboard) or checkcol(gameboard):
        print(f"The winner is {win}")
        gameActive = False

def switchplayer(gameboard):
    global player
    if player == "X":
        player = "0"
    else:
        player = "X"

while gameActive:
    printboard(gameboard)
    playerselect(gameboard)
    checkWin()
    checkTie(gameboard)
    switchplayer(gameboard)

