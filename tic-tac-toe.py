def add(a, b, c):
    return a + b + c


def printBoard(xState, oState):
    symbols = []
    for i in range(9):
        if xState[i]:
            symbols.append("X")
        elif oState[i]:
            symbols.append("O")
        else:
            symbols.append(str(i))

    print(f" {symbols[0]} | {symbols[1]} | {symbols[2]} ")
    print("---|---|---")
    print(f" {symbols[3]} | {symbols[4]} | {symbols[5]} ")
    print("---|---|---")
    print(f" {symbols[6]} | {symbols[7]} | {symbols[8]} ")


def checkWin(xState, oState):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for win in wins:
        if add(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X won the match")
            return 1
        if add(oState[win[0]], oState[win[1]], oState[win[2]]) == 3:
            print("O won the match")
            return 0
    return -1


if __name__ == "__main__":
    xState = [0] * 9
    oState = [0] * 9
    turn = 1  # 1 = X, 0 = O

    print("Welcome to Tic Tac Toe")

    while True:
        printBoard(xState, oState)

        if turn == 1:
            print("X's chance")
            value = int(input("Enter position (0-8): "))
            if xState[value] == 0 and oState[value] == 0:
                xState[value] = 1
            else:
                print("Invalid move!")
                continue
        else:
            print("O's chance")
            value = int(input("Enter position (0-8): "))
            if xState[value] == 0 and oState[value] == 0:
                oState[value] = 1
            else:
                print("Invalid move!")
                continue

        cwin = checkWin(xState, oState)
        if cwin != -1:
            print("Match over")
            break

        turn = 1 - turn
