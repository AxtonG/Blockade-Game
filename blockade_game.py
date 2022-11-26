from math import *


def gameboardfunc(Row, Col):
    global cola
    if Row >= 2:
        cola = []
        if Col >= 2:
            cola = []
            if Col <= 25:
                cola = []
                if Row <= 26:
                    cola = []
                    if int(Col % 2) == 1:
                        cola = []
                        for i in range(Row * 2 - 1):
                            rowa = []
                            cola.append(rowa)
                            for j in range(Col - 1):
                                if i % 2 == 1:
                                    rowa.append('-')
                                    rowa.append('.')
                                elif i % 2 != 1:
                                    rowa.append("'")
                                    rowa.append('|')
                            if i % 2 == 1:
                                rowa.append("-")
                            else:
                                rowa.append("'")
                        return print('\n'), print('------------------------------------------------------'), print(
                            'Perfect game board size!'), print("Player 1 "
                                                               "is piece "
                                                               "'0' and "
                                                               "Player 2 "
                                                               "is piece "
                                                               "'1'"), \
                               print('Players may choose to either move their piece towards the opposing side'), \
                               print('OR'), print('Players may choose to place a blockade blocking two '
                                                  'spots'), print(
                            '''Spots with the symbol "'" are spots you can move your piece'''), \
                               print("and spots that have either '.', '-', or '|' are spots to fill with "
                                     "blockades."), \
                               print('------------------------------------------------------'), print('\n')
                    else:
                        return print('\n \n \n'), print('Board is not playable, try a board that has an odd number of '
                                                        'columns!'), print('\n \n \n'), boardsize()
                else:
                    return print('\n \n \n'), print('Board is too big! Try a smaller board size'), print(
                        '\n \n \n'), boardsize()
            else:
                return print('\n \n \n'), print('Board is too big! Try a smaller board size'), print(
                    '\n \n \n'), boardsize()
        else:
            return print('\n \n \n'), print('Board is too small! Try a larger board size'), print(
                '\n \n \n'), boardsize()
    else:
        return print('\n \n \n'), print('Board is too small! Try a larger board size'), print('\n \n \n'), boardsize()


def boardsize():
    global Col, Row
    print('----------------------Board Size----------------------\n'
          'Max size is 26x25 and smallest size is 3x3 (Row x Columns)\n'
          'Keep Columns odd for game to work.\n'
          'Please enter number of Rows on gameboard: ', end='')
    Row = input()
    try:
        int(Row)
    except ValueError:
        i = 1
        while i == int(i):
            print('Enter a number silly.')
            print('Please enter number of Rows on gameboard: ', end='')
            Row = input()
            try:
                int(Row)
                break
            except ValueError:
                continue
    Row = int(Row)
    print('------------------------------------------------------\n'
          'Please enter number of Columns on gameboard: ', end='')
    Col = input()
    try:
        int(Col)
    except ValueError:
        i = 1
        while i == int(i):
            print('Enter a number silly.')
            print('Please enter number of Columns on gameboard: ', end='')
            Col = input()
            try:
                int(Col)
                break
            except ValueError:
                continue
    Col = int(Col)
    gameboardfunc(Row, Col)  # ask user for size of board (Row, Col) or (y, x), largest possible board is a 24 x 13
    return


boardsize()  # start of program
# Col variable must be odd
# assign player starting positions
PlayerOne = '0'
PlayerTwo = '1'
try:
    Col % 2 == 1
except TypeError:
    i = 0
    while i == int(i):
        print('Your dimensions must not be odd, fix this please.')
        boardsize()
        try:
            Col % 2 == 1
            break
        except TypeError:
            continue
if Col % 2 == 1:
    num = int(Col / 2) * 2
else:
    num = Col / 2
cola[0][num] = PlayerOne
cola[-1][num] = PlayerTwo
ColAssignments = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g',
                  'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N',
                  'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v',
                  'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'Z', 'z']


def drawboard():
    for i in range(len(cola)):
        for j in range(len(cola[i])):
            print(cola[i][j], end='')
        if i == 0:
            print(' a', end='')
        elif i == 1:
            print(' A', end='')
        elif i == 2:
            print(' b', end='')
        elif i == 3:
            print(' B', end='')
        elif i == 4:
            print(' c', end='')
        elif i == 5:
            print(' C', end='')
        elif i == 6:
            print(' d', end='')
        elif i == 7:
            print(' D', end='')
        elif i == 8:
            print(' e', end='')
        elif i == 9:
            print(' E', end='')
        elif i == 10:
            print(' f', end='')
        elif i == 11:
            print(' F', end='')
        elif i == 12:
            print(' g', end='')
        elif i == 13:
            print(' G', end='')
        elif i == 14:
            print(' h', end='')
        elif i == 15:
            print(' H', end='')
        elif i == 16:
            print(' i', end='')
        elif i == 17:
            print(' I', end='')
        elif i == 18:
            print(' j', end='')
        elif i == 19:
            print(' J', end='')
        elif i == 20:
            print(' k', end='')
        elif i == 21:
            print(' K', end='')
        elif i == 22:
            print(' l', end='')
        elif i == 23:
            print(' L', end='')
        elif i == 24:
            print(' m', end='')
        elif i == 25:
            print(' M', end='')
        elif i == 26:
            print(' n', end='')
        elif i == 27:
            print(' N', end='')
        elif i == 28:
            print(' o', end='')
        elif i == 29:
            print(' O', end='')
        elif i == 30:
            print(' p', end='')
        elif i == 31:
            print(' P', end='')
        elif i == 32:
            print(' q', end='')
        elif i == 33:
            print(' Q', end='')
        elif i == 34:
            print(' r', end='')
        elif i == 35:
            print(' R', end='')
        elif i == 36:
            print(' s', end='')
        elif i == 37:
            print(' S', end='')
        elif i == 38:
            print(' t', end='')
        elif i == 39:
            print(' T', end='')
        elif i == 40:
            print(' u', end='')
        elif i == 41:
            print(' U', end='')
        elif i == 42:
            print(' v', end='')
        elif i == 43:
            print(' V', end='')
        elif i == 44:
            print(' w', end='')
        elif i == 45:
            print(' W', end='')
        elif i == 46:
            print(' x', end='')
        elif i == 47:
            print(' X', end='')
        elif i == 48:
            print(' y', end='')
        elif i == 49:
            print(' Y', end='')
        elif i == 50:
            print(' z', end='')
        elif i == 51:
            print(' Z', end='')
        print('')
    for i in range(len(cola[0])):
        print(ColAssignments[i], end='')
    print('')
    return


drawboard()


def playersturn(player):
    global movelocation, blockadelocation
    while 1 == 1:
        print(f'---------------------------Player {player}---------------------------')
        print(f'Do you want to move your piece (M) or would you like to place a blockade (B): ', end='')
        choice = input()
        if choice == 'M':
            print(
                'You may only move your piece one gridspace away from your current location, diagonals are NOT included!')
            print(f"Please specify location that you want to move (side character then bottom, EX's --> aa, ea, "
                  f"bd): ", end='')
            movelocation = input()
            print('')
            print('')
            CheckPieceMovedOneGridSpace(movelocation,
                                        player)  # check for conditionals before using movepiece() function to actually move he piece  and gives GameIsGood Variable
            check4pinwhenmovingpin(player)  # gives space varialble
            checkifblockadeinway(player)
            if GameIsGood == True and space == True and blockadeNotinway == True:
                movepiece(movelocation, player)
                checkforwinner(player)
                if winnerexists == True:
                    print('------------------------------------------------------')
                    print('----------------------Game Over-----------------------')
                    print('------------------------------------------------------')
                    print(f'--------------------player {player} Won!---------------------')
                    print('------------------------------------------------------')

                    quit()
                elif winnerexists == False:
                    break
                break
            elif GameIsGood == False:
                print('Remember! You may only move ONE grid space away from your current location.')
                continue
            elif space == False:
                print('Sorry, but something is in the way!')
                continue
            elif blockadeNotinway == False:
                print('Looks like someone blocked this path, try moving a different direction')
                continue
            else:
                print('Follow the rules! Try a new spot.')
                print('')
                print('')
                continue
        elif choice == 'B':
            print(
                'You may place a blockade any place you choose, as long as it is \n NOT obstructed by another blockade or traps the opposing player')
            print(f"Please specify location that you want to place a blockade (side character then bottom), \n"
                  f"EX's --> AbAa): ", end='')
            blockadelocation = input()
            print('')
            print('')
            placeblockade(blockadelocation)
            break
    return


def movepiece(movelocation, player):
    move = list(movelocation)  # [ , ], bottom then side
    for i in range(len(move)):  # making list a set of int
        if move[i] == 'a':
            move[i] = 0
        elif move[i] == 'A':
            move[i] = 1
        elif move[i] == 'b':
            move[i] = 2
        elif move[i] == 'B':
            move[i] = 3
        elif move[i] == 'c':
            move[i] = 4
        elif move[i] == 'C':
            move[i] = 5
        elif move[i] == 'd':
            move[i] = 6
        elif move[i] == 'D':
            move[i] = 7
        elif move[i] == 'e':
            move[i] = 8
        elif move[i] == 'E':
            move[i] = 9
        elif move[i] == 'f':
            move[i] = 10
        elif move[i] == 'F':
            move[i] = 11
        elif move[i] == 'g':
            move[i] = 12
        elif move[i] == 'G':
            move[i] = 13
        elif move[i] == 'h':
            move[i] = 14
        elif move[i] == 'H':
            move[i] = 15
        elif move[i] == 'i':
            move[i] = 16
        elif move[i] == 'I':
            move[i] = 17
        elif move[i] == 'j':
            move[i] = 18
        elif move[i] == 'J':
            move[i] = 19
        elif move[i] == 'k':
            move[i] = 20
        elif move[i] == 'K':
            move[i] = 21
        elif move[i] == 'l':
            move[i] = 22
        elif move[i] == 'L':
            move[i] = 23
        elif move[i] == 'm':
            move[i] = 24
        elif move[i] == 'M':
            move[i] = 25
        elif move[i] == 'n':
            move[i] = 26
        elif move[i] == 'N':
            move[i] = 27
        elif move[i] == 'o':
            move[i] = 28
        elif move[i] == 'O':
            move[i] = 29
        elif move[i] == 'p':
            move[i] = 30
        elif move[i] == 'P':
            move[i] = 31
        elif move[i] == 'q':
            move[i] = 32
        elif move[i] == 'Q':
            move[i] = 33
        elif move[i] == 'r':
            move[i] = 34
        elif move[i] == 'R':
            move[i] = 35
        elif move[i] == 's':
            move[i] = 36
        elif move[i] == 'S':
            move[i] = 37
        elif move[i] == 't':
            move[i] = 38
        elif move[i] == 'T':
            move[i] = 39
        elif move[i] == 'u':
            move[i] = 40
        elif move[i] == 'U':
            move[i] = 41
        elif move[i] == 'v':
            move[i] = 42
        elif move[i] == 'V':
            move[i] = 43
        elif move[i] == 'w':
            move[i] = 44
        elif move[i] == 'W':
            move[i] = 45
        elif move[i] == 'x':
            move[i] = 46
        elif move[i] == 'X':
            move[i] = 47
        elif move[i] == 'y':
            move[i] = 48
        elif move[i] == 'Y':
            move[i] = 49
        elif move[i] == 'z':
            move[i] = 50
        elif move[i] == 'Z':
            move[i] = 51
    if player == 1:
        MoveLogPlayerOne.append(move)
        cola[MoveLogPlayerOne[n1][0]][MoveLogPlayerOne[n1][1]] = "'"
        cola[move[0]][move[1]] = '0'
    elif player == 2:
        MoveLogPlayerTwo.append(move)
        cola[MoveLogPlayerTwo[n2][0]][MoveLogPlayerTwo[n2][1]] = "'"
        cola[move[0]][move[1]] = '1'
    return


def placeblockade(blockadelocation):
    global block
    block = list(blockadelocation)  # [ , , , ]
    for i in range(len(block)):
        if block[i] == 'a':
            block[i] = 0
        elif block[i] == 'A':
            block[i] = 1
        elif block[i] == 'b':
            block[i] = 2
        elif block[i] == 'B':
            block[i] = 3
        elif block[i] == 'c':
            block[i] = 4
        elif block[i] == 'C':
            block[i] = 5
        elif block[i] == 'd':
            block[i] = 6
        elif block[i] == 'D':
            block[i] = 7
        elif block[i] == 'e':
            block[i] = 8
        elif block[i] == 'E':
            block[i] = 9
        elif block[i] == 'f':
            block[i] = 10
        elif block[i] == 'F':
            block[i] = 11
        elif block[i] == 'g':
            block[i] = 12
        elif block[i] == 'G':
            block[i] = 13
        elif block[i] == 'h':
            block[i] = 14
        elif block[i] == 'H':
            block[i] = 15
        elif block[i] == 'i':
            block[i] = 16
        elif block[i] == 'I':
            block[i] = 17
        elif block[i] == 'j':
            block[i] = 18
        elif block[i] == 'J':
            block[i] = 19
        elif block[i] == 'k':
            block[i] = 20
        elif block[i] == 'K':
            block[i] = 21
        elif block[i] == 'l':
            block[i] = 22
        elif block[i] == 'L':
            block[i] = 23
        elif block[i] == 'm':
            block[i] = 24
        elif block[i] == 'M':
            block[i] = 25
        elif block[i] == 'n':
            block[i] = 26
        elif block[i] == 'N':
            block[i] = 27
        elif block[i] == 'o':
            block[i] = 28
        elif block[i] == 'O':
            block[i] = 29
        elif block[i] == 'p':
            block[i] = 30
        elif block[i] == 'P':
            block[i] = 31
        elif block[i] == 'q':
            block[i] = 32
        elif block[i] == 'Q':
            block[i] = 33
        elif block[i] == 'r':
            block[i] = 34
        elif block[i] == 'R':
            block[i] = 35
        elif block[i] == 's':
            block[i] = 36
        elif block[i] == 'S':
            block[i] = 37
        elif block[i] == 't':
            block[i] = 38
        elif block[i] == 'T':
            block[i] = 39
        elif block[i] == 'u':
            block[i] = 40
        elif block[i] == 'U':
            block[i] = 41
        elif block[i] == 'v':
            block[i] = 42
        elif block[i] == 'V':
            block[i] = 43
        elif block[i] == 'w':
            block[i] = 44
        elif block[i] == 'W':
            block[i] = 45
        elif block[i] == 'x':
            block[i] = 46
        elif block[i] == 'X':
            block[i] = 47
        elif block[i] == 'y':
            block[i] = 48
        elif block[i] == 'Y':
            block[i] = 49
        elif block[i] == 'z':
            block[i] = 50
        elif block[i] == 'Z':
            block[i] = 51
    if block[0] == block[2]:  # horizontal blockades
        cola[block[0]][block[1]] = '='
        cola[block[2]][block[3]] = '='
        if block[1] > block[3]:
            diff = int((block[1] + block[3]) / 2)
            cola[block[0]][diff] = '='
        elif block[1] < block[3]:
            diff = int((block[3] + block[1]) / 2)
            cola[block[0]][diff] = '='
    elif block[1] == block[3]:  # vertical blockades
        cola[block[0]][block[1]] = '='
        cola[block[2]][block[3]] = '='
        if block[0] > block[2]:
            diff = int((block[0] + block[2]) / 2)
            cola[diff][block[3]] = '='
        elif block[0] < block[2]:
            diff = int((block[2] + block[0]) / 2)
            cola[diff][block[3]] = '='
    return


MoveLogPlayerOne = [[0, num]]
MoveLogPlayerTwo = [[int((len(cola) - 1)), num]]


def CheckPieceMovedOneGridSpace(movelocation, player):
    global n1, n2, move
    n1 = len(MoveLogPlayerOne) - 1
    n2 = len(MoveLogPlayerTwo) - 1
    global GameIsGood
    move = list(movelocation)  # [ , ], bottom then side
    for i in range(len(move)):  # making list a set of int
        if move[i] == 'a':
            move[i] = 0
        elif move[i] == 'A':
            move[i] = 1
        elif move[i] == 'b':
            move[i] = 2
        elif move[i] == 'B':
            move[i] = 3
        elif move[i] == 'c':
            move[i] = 4
        elif move[i] == 'C':
            move[i] = 5
        elif move[i] == 'd':
            move[i] = 6
        elif move[i] == 'D':
            move[i] = 7
        elif move[i] == 'e':
            move[i] = 8
        elif move[i] == 'E':
            move[i] = 9
        elif move[i] == 'f':
            move[i] = 10
        elif move[i] == 'F':
            move[i] = 11
        elif move[i] == 'g':
            move[i] = 12
        elif move[i] == 'G':
            move[i] = 13
        elif move[i] == 'h':
            move[i] = 14
        elif move[i] == 'H':
            move[i] = 15
        elif move[i] == 'i':
            move[i] = 16
        elif move[i] == 'I':
            move[i] = 17
        elif move[i] == 'j':
            move[i] = 18
        elif move[i] == 'J':
            move[i] = 19
        elif move[i] == 'k':
            move[i] = 20
        elif move[i] == 'K':
            move[i] = 21
        elif move[i] == 'l':
            move[i] = 22
        elif move[i] == 'L':
            move[i] = 23
        elif move[i] == 'm':
            move[i] = 24
        elif move[i] == 'M':
            move[i] = 25
        elif move[i] == 'n':
            move[i] = 26
        elif move[i] == 'N':
            move[i] = 27
        elif move[i] == 'o':
            move[i] = 28
        elif move[i] == 'O':
            move[i] = 29
        elif move[i] == 'p':
            move[i] = 30
        elif move[i] == 'P':
            move[i] = 31
        elif move[i] == 'q':
            move[i] = 32
        elif move[i] == 'Q':
            move[i] = 33
        elif move[i] == 'r':
            move[i] = 34
        elif move[i] == 'R':
            move[i] = 35
        elif move[i] == 's':
            move[i] = 36
        elif move[i] == 'S':
            move[i] = 37
        elif move[i] == 't':
            move[i] = 38
        elif move[i] == 'T':
            move[i] = 39
        elif move[i] == 'u':
            move[i] = 40
        elif move[i] == 'U':
            move[i] = 41
        elif move[i] == 'v':
            move[i] = 42
        elif move[i] == 'V':
            move[i] = 43
        elif move[i] == 'w':
            move[i] = 44
        elif move[i] == 'W':
            move[i] = 45
        elif move[i] == 'x':
            move[i] = 46
        elif move[i] == 'X':
            move[i] = 47
        elif move[i] == 'y':
            move[i] = 48
        elif move[i] == 'Y':
            move[i] = 49
        elif move[i] == 'z':
            move[i] = 50
        elif move[i] == 'Z':
            move[i] = 51
    # player one check
    if player == 1:
        if move[0] == MoveLogPlayerOne[n1][0]:  # moving side to side
            diff = MoveLogPlayerOne[n1][1] - move[1]
            if diff == 2:
                GameIsGood = True
            elif diff == -1 * 2:
                GameIsGood = True
            else:
                GameIsGood = False
        elif move[1] == MoveLogPlayerOne[n1][1]:  # moving up or down
            diff = MoveLogPlayerOne[n1][0] - move[0]
            if diff == 2:
                GameIsGood = True
            elif diff == -1 * 2:
                GameIsGood = True
            else:
                GameIsGood = False
        else:
            GameIsGood = False
    # player two check
    if player == 2:
        if move[0] == MoveLogPlayerTwo[n2][0]:  # moving side to side
            diff = MoveLogPlayerTwo[n2][1] - move[1]
            if diff == 2:
                GameIsGood = True
            elif diff == -1 * 2:
                GameIsGood = True
            else:
                GameIsGood = False
        elif move[1] == MoveLogPlayerTwo[n2][1]:  # moving up or down
            diff = MoveLogPlayerTwo[n2][0] - move[0]
            if diff == 2:
                GameIsGood = True
            elif diff == -1 * 2:
                GameIsGood = True
            else:
                GameIsGood = False
        else:
            GameIsGood = False
    return


def check4pinwhenmovingpin(player):
    global space
    if player == 1:
        if move != MoveLogPlayerTwo[n2]:
            space = True
        elif move == MoveLogPlayerTwo[n2]:
            space = False
    elif player == 2:
        if move != MoveLogPlayerOne[n1]:
            space = True
        elif move == MoveLogPlayerOne[n1]:
            space = False
    return


def checkifblockadeinway(player):
    global move, blockadeNotinway
    move1 = move
    if player == 1:
        if move1[0] == MoveLogPlayerOne[n1][0]:  # movement of pin is horizontal and blockade may be vertical
            if move1[1] < MoveLogPlayerOne[n1][1]:
                move1[1] = move1[1] + 1
            elif move1[1] > MoveLogPlayerOne[n1][1]:
                move1[1] = move1[1] - 1
        elif move1[1] == MoveLogPlayerOne[n1][1]:  # movement of pin is vertical and blockade may be horizontal
            if move1[0] < MoveLogPlayerOne[n1][0]:
                move1[0] = move1[0] + 1
            elif move1[0] > MoveLogPlayerOne[n1][0]:
                move1[0] = move1[0] - 1
    elif player == 2:
        if move1[0] == MoveLogPlayerTwo[n2][0]:  # movement of pin is horizontal and blockade may be vertical
            if move1[1] < MoveLogPlayerTwo[n2][1]:
                move1[1] = move1[1] + 1
            elif move1[1] > MoveLogPlayerTwo[n2][1]:
                move1[1] = move1[1] - 1
        elif move1[1] == MoveLogPlayerTwo[n2][1]:  # movement of pin is vertical and blockade may be horizontal
            if move1[0] < MoveLogPlayerTwo[n2][0]:
                move1[0] = move1[0] + 1
            elif move1[0] > MoveLogPlayerTwo[n2][0]:
                move1[0] = move1[0] - 1
    if cola[move[0]][move[1]] == '=':
        blockadeNotinway = False
    else:
        blockadeNotinway = True
    return


def checkforwinner(player):
    global winnerexists
    if player == 2:
        if '1' in cola[0]:
            winnerexists = True
        else:
            winnerexists = False
    elif player == 1:
        if '0' in cola[-1]:
            winnerexists = True
        else:
            winnerexists = False
    return


GameIsRunning = True
while 1 == 1:
    if GameIsRunning == True:
        playersturn(1)
        drawboard()
        playersturn(2)
        drawboard()
    elif GameIsRunning == False:
        print(f'Congratulations Player {player}! You have won the game, want to play again?')
        break

