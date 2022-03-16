import sys

Boad_Colunm = 7
Boad_Row = 6

COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')

Empty_Space = "."
Player_X = "X"
Player_O = "O"

def main():
    gameBoard = getNewBoard()
    playerTurn = Player_X

    while True:
        displayBoard(gameBoard)

        playerMove = askForPlayerMove(playerTurn,gameBoard)
        gameBoard[playerMove] = playerTurn





def getNewBoard():
    boad = {}
    for column in range(Boad_Colunm):
        for row in range(Boad_Row):
            boad[(column,row)] = Empty_Space

    return boad


def displayBoard(board):
    tileChars = []
    for column in range(Boad_Colunm):
        for row in range(Boad_Row):
            tileChars.append(board[(column,row)])
    print("""
         1234567
        +-------+
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        +-------+""".format(*tileChars))


def askForPlayerMove(playerTurn,gameBoard):
    while True:
        enter = input(">").upper().strip()

        if enter == "QUIT":
            sys.exit()

        if enter not in COLUMN_LABELS:
            print('Enter a number from 1 to {}.'.format(Boad_Colunm))
            continue

        column_index = int(enter) - 1
        if gameBoard[(column_index,0)] != Empty_Space:
            print('That column is full, select another one.')
            continue

        for row_index in range(Boad_Row-1,-1,-1):
            if gameBoard[(column_index,row_index)] == Empty_Space:
                return (column_index,row_index)





if __name__ == "__main__":
    main()