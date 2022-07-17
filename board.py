gameboard = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
player = "X"
gameCurrent = True
win = None

def printboard(gameboard):
    print(gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2])
    print("")
    print(gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5])
    print("")
    print(gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8])
printboard(gameboard)


