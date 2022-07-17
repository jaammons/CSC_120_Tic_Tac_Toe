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

def playerInput(gameboard):
    inp = int(input("Select a number 0-8: "))
    if inp >= 0 and inp < 9 and gameboard[inp] == "-":
        gameboard[inp] = player
    else:
        print("This spot is taken by another player!")

while gameCurrent:
    printboard(gameboard)
    playerInput(gameboard)
