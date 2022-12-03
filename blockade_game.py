from math import *
import turtle
import time


def gameboardfunc(Row, Col):
    """
    This function takes input (Row and Col) from user and outputs a matrix
    Function also globalizes cola(the matrix) for future use
    :param Row: Input from user, signifying row count
    :param Col: Input from user, signifying col count
    :return: returns list of rules ONLY if all rules (conditionals)
             are met, if not, the program prints a message saying what failed and returns user
             to input func
    """
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
    """
    This functions takes no parameters and asks user for input on board size, should be first functions called in program
    :return: function returns nothing, but globalizes inputs (Row and Col)
    """
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

# -----------------------------------------



# this can probably be removed or corrected v



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

# -----------------------------------------

ColAssignments = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g',
                  'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N',
                  'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v',
                  'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'Z', 'z']

def drawboard():
    """
    FUNCTION IS CURRENTLY USELESS UNLESS FOR CHECKING
    This function was essentially used for testing before turtle graphics were utilized
    The function prints the board out on python console and adds the board grid assignments a-z
    based on size of board.
    :return: there are no returns, simply prints boards on console if used
    """
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

#  this is probably most used functions, as it runs it also runs just about every conditinal functions as well
#  Each player move and blockade placement is checked through other functions before being placed through this function
def playersturn(player):
    """
    This function asks user to either move piece or place blockade and checks every conditional
    property (rule)
    :param player: Takes parameter player, to know which player's turn it is
    :return: This functions globalizes the movelocation or blockadelocation based on user
             input. Returns nothing.
    """
    global movelocation, blockadelocation
    while 1 == 1:
        print(f'---------------------------Player {player}---------------------------')
        print(f'Do you want to move your piece (M) or would you like to place a blockade (B): ', end='')
        choice = input()
        if choice == 'M' or choice == 'm':
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
        elif choice == 'B' or choice == 'b':
            print(
                'You may place a blockade any place you choose, as long as it is \n NOT obstructed by another blockade or traps the opposing player')
            print(f"Please specify location that you want to place a blockade (side character then bottom), \n"
                  f"EX's --> AbAa): ", end='')
            blockadelocation = input()
            print('')
            print('')
            # check conditional that block input is within boundaries
            checkblockade(blockadelocation)
            if coastisclear == True:
                placeblockade(blockadelocation)
                break
            else:
                print('The desired blockade is not possible, make sure the length is accurate')
                continue
        else:
            print('Please enter a valid input.')
            continue
    return


def checkblockade(blockadelocation):
    """
    This function takes blockadelocation (input of location from user wanting to place a blockade)
    It first converts the 4-letter string to a number list (4 len) to easily find location on matrix
    and then checks if the location input is reasonable/ right size, if it isn't it returns False
    :param blockadelocation: Takes parameter, location which is a 4 character string of letter assignments
    :return: Function returns nothing. Globalizes costisclear which comes back as either boolean True or False
    """
    global coastisclear
    block = list(blockadelocation)  # [ , , , ]
    for i in range(len(block)):  # this takes blockadelocation list input [ , , , ]
                                 # and converts it into a list of numbers for use in matrix
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
    if block[0] == block[2]:
        diff = abs(block[1] - block[3])
        if diff == 2:
            coastisclear = True
        else:
            coastisclear = False
    elif block[1] == block[3]:
        diff = abs(block[0] - block[2])
        if diff == 2:
            coastisclear = True
        else:
            coastisclear = False
    return


def movepiece(movelocation, player):
    """
    Function places player pin based on player number and movelocation
    :param movelocation: This parameter takes the input of location (2-character input from letter assignment)
    :param player: This parameter takes into account which player is actually moving
    :return: function returns nothing and gloalizes nothing, but alters the gameboard matrix (cola) and places the players pin where they decided to move.
    """
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
    """
    This function places the blockade in the gameboard matrix (cola)
    :param blockadelocation: takes input on location from user for where blockade to be placed
    :return: returns nothing, globalizes block (list of the blockade location with numbers)
    """
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

# here i assigned two move logs, which tracks the last position the players pin were in
# this is used for a later function that utilizes the previous move to remove the pin and update the gameboard so that...
# there is not more than one player # pin at once
MoveLogPlayerOne = [[0, num]]
MoveLogPlayerTwo = [[int((len(cola) - 1)), num]]


def CheckPieceMovedOneGridSpace(movelocation, player):
    """
    This function checks that the player is moving ONLY one grid space away from previous position
    used the 'MoveLogPlayer{}' list to check
    :param movelocation: takes param movelocation to compare to original position
    :param player: takes param player to know which player is moving and which list of move logs to access
    :return: returns nothing, globalizes GameIsGood which is boolean True or False, either allowing the game to continue(if rules were followed) or not.
             also globalizes n1 and n2, which are the last move the player made (takes len(MoveLogPlayer{}) - 1, giving an index number for latest move).
             Function also globalizes move which is the list of number sof the desired location to move from player{}
    """
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
    """
    This function checks if the desired position to move is currently occupied by the other players pin, if so, then variable returns as False, if not the function returns as True
    :param player: Takes param player to know whos turn it is
    :return: returns nothing, globalizes space which returns as either boolean True or False
    """
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
    """
    This function checks if players desired move location is blocked by a blockade
    :param player: Takse param player
    :return: returns nothing, globalizes blockadeNotinway which returns as boolena true or false
    """
    global move, blockadeNotinway  # i haven't checked, but globalizing move may not be necessary at all. Nothing changes move here so im not sure why i did that
    move1 = move  # im pretty sure i did this, because i was having some weird error that i couldn't figure out but this seemed to fix it
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
    """
    This function checks for playes pin to be on the opposing side of the board (last row, opposite side)
    :param player: takes param player
    :return: returns nothing, globalizes winnerexists which returns as either boolean true or false.
    """
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




# THIS IS WHERE TURTLE GRAPHICS BEGIN
# the turtle graphics take the matrix (cola), and prints it out on turtle



def drawgame(cola):  # simply draw out the 2D matrix of the gameboard after each turn is taken by player.
    """
    This function essentially draws out the entire gameboard on turtle, utilizes all the future functions
    :param cola: takes param cola, which is the matrix that is constantly being updates after each player turn
    :return: function returns nothing, globalizes gameboard for other functions to use for turtle graphics.
    """
    # use turtle.setworldcordinates to change aspect ratio and make the board fit on the screen if larger
    # or smaller
    global gameboard
    turtle.tracer(0, 0)
    gameboard = turtle.Turtle()
    # this section (4lines below) trys to make a proportionally sized board for the size of window opened for turtle
    x2colbigger = len(cola[0]) * 19
    y1colbigger = -(len(cola[0]) * 19)
    x2rowbigger = len(cola) * 19
    y1rowbigger = -(len(cola) * 19)
    if len(cola[0]) >= len(cola):
        turtle.setworldcoordinates(0, y1colbigger, x2colbigger, 0)
        gameboard.penup()
        gameboard.goto(x2colbigger, y1colbigger)
        gameboard.write('BLOCKADE\n'
                        'Objective: Move pin across board\n'
                        'Player 1 = Maroon     Player 2 = Grey\n'
                        'Choose grid space by assigning side letter x bottom letter\n'
                        'Moving your piece only requires a 2 character input, while...\n'
                        'placing a blockade/barrier requires a 4 character input, and\n'
                        'covers two empty spaces between two grid spaces\n'
                        'Capital letters are for the spaces between gridspots while,\n'
                        'lower case letters are for grid spots.', font=("Arial", 7, "bold"), align='right')
        gameboard.goto(0, 0)
        gameboard.pendown()
    elif len(cola[0]) < len(cola):
        turtle.setworldcoordinates(0, y1rowbigger, x2rowbigger, 0)
        gameboard.penup()
        gameboard.goto(x2rowbigger, y1rowbigger)
        gameboard.write('BLOCKADE\n'
                        'Objective: Move pin across board\n'
                        'Player 1 = Maroon     Player 2 = Grey\n'
                        'Choose grid space by assigning side letter x bottom letter\n'
                        'Moving your piece only requires a 2 character input, while...\n'
                        'placing a blockade/barrier requires a 4 character input, and\n'
                        'covers two empty spaces between two grid spaces\n'
                        'Capital letters are for the spaces between gridspots while,\n'
                        'lower case letters are for grid spots.', font=("Arial", 7, "bold"), align='right')
        gameboard.goto(0, 0)
        gameboard.pendown()
    # add description on bottom left of screen
    for i in range(len(cola)):  # want order drawn to be like a book, as read by the matrix by python (top left to bottom right)
        if i >= 1:
            if i % 2 != 0:  # odd
                # add text/ way for assigning grid spaces/ blockade spaces a value ex- aa, AaAb, etc...
                if i >= 1:  # declaring not last row
                    if i == 1:
                        movetotextBIG(gameboard)
                        gameboard.write('a')
                        moveawayfromtextBIG(gameboard)
                    elif i == 3:
                        movetotextBIG(gameboard)
                        gameboard.write('b')
                        moveawayfromtextBIG(gameboard)
                    elif i == 5:
                        movetotextBIG(gameboard)
                        gameboard.write('c')
                        moveawayfromtextBIG(gameboard)
                    elif i == 7:
                        movetotextBIG(gameboard)
                        gameboard.write('d')
                        moveawayfromtextBIG(gameboard)
                    elif i == 9:
                        movetotextBIG(gameboard)
                        gameboard.write('e')
                        moveawayfromtextBIG(gameboard)
                    elif i == 11:
                        movetotextBIG(gameboard)
                        gameboard.write('f')
                        moveawayfromtextBIG(gameboard)
                    elif i == 13:
                        movetotextBIG(gameboard)
                        gameboard.write('g')
                        moveawayfromtextBIG(gameboard)
                    elif i == 15:
                        movetotextBIG(gameboard)
                        gameboard.write('h')
                        moveawayfromtextBIG(gameboard)
                    elif i == 17:
                        movetotextBIG(gameboard)
                        gameboard.write('i')
                        moveawayfromtextBIG(gameboard)
                    elif i == 19:
                        movetotextBIG(gameboard)
                        gameboard.write('j')
                        moveawayfromtextBIG(gameboard)
                    elif i == 21:
                        movetotextBIG(gameboard)
                        gameboard.write('k')
                        moveawayfromtextBIG(gameboard)
                    elif i == 23:
                        movetotextBIG(gameboard)
                        gameboard.write('l')
                        moveawayfromtextBIG(gameboard)
                    elif i == 25:
                        movetotextBIG(gameboard)
                        gameboard.write('m')
                        moveawayfromtextBIG(gameboard)
                    elif i == 27:
                        movetotextBIG(gameboard)
                        gameboard.write('n')
                        moveawayfromtextBIG(gameboard)
                    elif i == 29:
                        movetotextBIG(gameboard)
                        gameboard.write('o')
                        moveawayfromtextBIG(gameboard)
                    elif i == 31:
                        movetotextBIG(gameboard)
                        gameboard.write('p')
                        moveawayfromtextBIG(gameboard)
                    elif i == 33:
                        movetotextBIG(gameboard)
                        gameboard.write('q')
                        moveawayfromtextBIG(gameboard)
                    elif i == 35:
                        movetotextBIG(gameboard)
                        gameboard.write('r')
                        moveawayfromtextBIG(gameboard)
                    elif i == 37:
                        movetotextBIG(gameboard)
                        gameboard.write('s')
                        moveawayfromtextBIG(gameboard)
                    elif i == 39:
                        movetotextBIG(gameboard)
                        gameboard.write('t')
                        moveawayfromtextBIG(gameboard)
                    elif i == 41:
                        movetotextBIG(gameboard)
                        gameboard.write('u')
                        moveawayfromtextBIG(gameboard)
                    elif i == 43:
                        movetotextBIG(gameboard)
                        gameboard.write('v')
                        moveawayfromtextBIG(gameboard)
                    elif i == 45:
                        movetotextBIG(gameboard)
                        gameboard.write('w')
                        moveawayfromtextBIG(gameboard)
                    elif i == 47:
                        movetotextBIG(gameboard)
                        gameboard.write('x')
                        moveawayfromtextBIG(gameboard)
                    elif i == 49:
                        movetotextBIG(gameboard)
                        gameboard.write('y')
                        moveawayfromtextBIG(gameboard)
                    elif i == 51:
                        movetotextBIG(gameboard)
                        gameboard.write('z')
                        moveawayfromtextBIG(gameboard)
                if i == len(cola) - 2:  # last row
                    if i == 3:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('c')
                        fromlastrowtextBIG(gameboard)
                    elif i == 5:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('d')
                        fromlastrowtextBIG(gameboard)
                    elif i == 7:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('e')
                        fromlastrowtextBIG(gameboard)
                    elif i == 9:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('f')
                        fromlastrowtextBIG(gameboard)
                    elif i == 11:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('g')
                        fromlastrowtextBIG(gameboard)
                    elif i == 13:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('h')
                        fromlastrowtextBIG(gameboard)
                    elif i == 15:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('i')
                        fromlastrowtextBIG(gameboard)
                    elif i == 17:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('j')
                        fromlastrowtextBIG(gameboard)
                    elif i == 19:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('k')
                        fromlastrowtextBIG(gameboard)
                    elif i == 21:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('l')
                        fromlastrowtextBIG(gameboard)
                    elif i == 23:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('m')
                        fromlastrowtextBIG(gameboard)
                    elif i == 25:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('n')
                        fromlastrowtextBIG(gameboard)
                    elif i == 27:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('o')
                        fromlastrowtextBIG(gameboard)
                    elif i == 29:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('p')
                        fromlastrowtextBIG(gameboard)
                    elif i == 31:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('q')
                        fromlastrowtextBIG(gameboard)
                    elif i == 33:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('r')
                        fromlastrowtextBIG(gameboard)
                    elif i == 35:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('s')
                        fromlastrowtextBIG(gameboard)
                    elif i == 37:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('t')
                        fromlastrowtextBIG(gameboard)
                    elif i == 39:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('u')
                        fromlastrowtextBIG(gameboard)
                    elif i == 41:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('v')
                        fromlastrowtextBIG(gameboard)
                    elif i == 43:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('w')
                        fromlastrowtextBIG(gameboard)
                    elif i == 45:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('x')
                        fromlastrowtextBIG(gameboard)
                    elif i == 47:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('y')
                        fromlastrowtextBIG(gameboard)
                    elif i == 49:
                        tolastrowtextBIG(gameboard)
                        gameboard.write('z')
                        fromlastrowtextBIG(gameboard)
                resetturtleeven(gameboard)
            elif i % 2 == 0:  # even
                if i == 2:
                    movetotextLITTLE(gameboard)
                    gameboard.write('A')
                    movefromtextLITTLE(gameboard)
                elif i == 4:
                    movetotextLITTLE(gameboard)
                    gameboard.write('B')
                    movefromtextLITTLE(gameboard)
                elif i == 6:
                    movetotextLITTLE(gameboard)
                    gameboard.write('C')
                    movefromtextLITTLE(gameboard)
                elif i == 8:
                    movetotextLITTLE(gameboard)
                    gameboard.write('D')
                    movefromtextLITTLE(gameboard)
                elif i == 10:
                    movetotextLITTLE(gameboard)
                    gameboard.write('E')
                    movefromtextLITTLE(gameboard)
                elif i == 12:
                    movetotextLITTLE(gameboard)
                    gameboard.write('F')
                    movefromtextLITTLE(gameboard)
                elif i == 14:
                    movetotextLITTLE(gameboard)
                    gameboard.write('G')
                    movefromtextLITTLE(gameboard)
                elif i == 16:
                    movetotextLITTLE(gameboard)
                    gameboard.write('H')
                    movefromtextLITTLE(gameboard)
                elif i == 18:
                    movetotextLITTLE(gameboard)
                    gameboard.write('I')
                    movefromtextLITTLE(gameboard)
                elif i == 20:
                    movetotextLITTLE(gameboard)
                    gameboard.write('J')
                    movefromtextLITTLE(gameboard)
                elif i == 22:
                    movetotextLITTLE(gameboard)
                    gameboard.write('K')
                    movefromtextLITTLE(gameboard)
                elif i == 24:
                    movetotextLITTLE(gameboard)
                    gameboard.write('L')
                    movefromtextLITTLE(gameboard)
                elif i == 26:
                    movetotextLITTLE(gameboard)
                    gameboard.write('M')
                    movefromtextLITTLE(gameboard)
                elif i == 28:
                    movetotextLITTLE(gameboard)
                    gameboard.write('N')
                    movefromtextLITTLE(gameboard)
                elif i == 30:
                    movetotextLITTLE(gameboard)
                    gameboard.write('O')
                    movefromtextLITTLE(gameboard)
                elif i == 32:
                    movetotextLITTLE(gameboard)
                    gameboard.write('P')
                    movefromtextLITTLE(gameboard)
                elif i == 34:
                    movetotextLITTLE(gameboard)
                    gameboard.write('Q')
                    movefromtextLITTLE(gameboard)
                elif i == 36:
                    movetotextLITTLE(gameboard)
                    gameboard.write('R')
                    movefromtextLITTLE(gameboard)
                elif i == 38:
                    movetotextLITTLE(gameboard)
                    gameboard.write('S')
                    movefromtextLITTLE(gameboard)
                elif i == 40:
                    movetotextLITTLE(gameboard)
                    gameboard.write('T')
                    movefromtextLITTLE(gameboard)
                elif i == 42:
                    movetotextLITTLE(gameboard)
                    gameboard.write('U')
                    movefromtextLITTLE(gameboard)
                elif i == 44:
                    movetotextLITTLE(gameboard)
                    gameboard.write('V')
                    movefromtextLITTLE(gameboard)
                elif i == 46:
                    movetotextLITTLE(gameboard)
                    gameboard.write('W')
                    movefromtextLITTLE(gameboard)
                elif i == 48:
                    movetotextLITTLE(gameboard)
                    gameboard.write('X')
                    movefromtextLITTLE(gameboard)
                elif i == 50:
                    movetotextLITTLE(gameboard)
                    gameboard.write('Y')
                    movefromtextLITTLE(gameboard)
                elif i == 52:
                    movetotextLITTLE(gameboard)
                    gameboard.write('Z')
                    movefromtextLITTLE(gameboard)
                resetturtleodd(gameboard)
        for j in range(len(cola[i])):
            if i % 2 == 0:  # know if blockade even, thus blockade will be standing up right / vertical
                if cola[i][j] == "'":  # grid spot
                    drawgridspace(gameboard)
                elif cola[i][j] == '|':  # empty space vertical
                    drawemptyspacevert(gameboard)
                elif cola[i][j] == '0':  # player1 pin
                    drawplayeronepin(gameboard)
                elif cola[i][j] == '1':  # player2 pin
                    drawplayertwopin(gameboard)
                elif cola[i][j] == '=':  # blockade
                    drawblockadevert(gameboard)
            else:  # everything else is odd, thus blockade will be laying sideways / horizontal and no pins should exist
                if cola[i][j] == '-':  # empty space horizontal
                    drawemptyspacehor(gameboard)
                elif cola[i][j] == '.':  # empty space intersections
                    drawintersectingemptyspace(gameboard)
                elif cola[i][j] == '=':  # blockade
                    if j % 2 == 0:
                        drawhorizontalblockade(gameboard)
                    elif j % 2 != 0:
                        drawintersectingblockade(gameboard)
    resetturtleeven(gameboard)
    gameboard.penup()
    gameboard.right(90)
    gameboard.forward(15)
    gameboard.left(90)
    gameboard.forward(7)
    gameboard.write('a')
    for i in range(len(cola[0])):
        if i % 2 == 0: # even/ for gridspace assignments
            if i == 2:
                move2text(gameboard)
                gameboard.write('b')
            elif i == 4:
                move2text(gameboard)
                gameboard.write('c')
            elif i == 6:
                move2text(gameboard)
                gameboard.write('d')
            elif i == 8:
                move2text(gameboard)
                gameboard.write('e')
            elif i == 10:
                move2text(gameboard)
                gameboard.write('f')
            elif i == 12:
                move2text(gameboard)
                gameboard.write('g')
            elif i == 14:
                move2text(gameboard)
                gameboard.write('h')
            elif i == 16:
                move2text(gameboard)
                gameboard.write('i')
            elif i == 18:
                move2text(gameboard)
                gameboard.write('j')
            elif i == 20:
                move2text(gameboard)
                gameboard.write('k')
            elif i == 22:
                move2text(gameboard)
                gameboard.write('l')
            elif i == 24:
                move2text(gameboard)
                gameboard.write('m')
            elif i == 26:
                move2text(gameboard)
                gameboard.write('n')
            elif i == 28:
                move2text(gameboard)
                gameboard.write('o')
            elif i == 30:
                move2text(gameboard)
                gameboard.write('p')
            elif i == 32:
                move2text(gameboard)
                gameboard.write('q')
            elif i == 34:
                move2text(gameboard)
                gameboard.write('r')
            elif i == 36:
                move2text(gameboard)
                gameboard.write('s')
            elif i == 38:
                move2text(gameboard)
                gameboard.write('t')
            elif i == 40:
                move2text(gameboard)
                gameboard.write('u')
            elif i == 42:
                move2text(gameboard)
                gameboard.write('v')
            elif i == 44:
                move2text(gameboard)
                gameboard.write('w')
            elif i == 46:
                move2text(gameboard)
                gameboard.write('x')
            elif i == 48:
                move2text(gameboard)
                gameboard.write('y')
            elif i == 50:
                move2text(gameboard)
                gameboard.write('z')
        elif i % 2 != 0:  # odd / blockade spaces assignments (write text)
            if i == 1:
                moveout(gameboard)
                gameboard.write('A')
                movein(gameboard)
            elif i == 3:
                moveout(gameboard)
                gameboard.write('B')
                movein(gameboard)
            elif i == 5:
                moveout(gameboard)
                gameboard.write('C')
                movein(gameboard)
            elif i == 7:
                moveout(gameboard)
                gameboard.write('D')
                movein(gameboard)
            elif i == 9:
                moveout(gameboard)
                gameboard.write('E')
                movein(gameboard)
            elif i == 11:
                moveout(gameboard)
                gameboard.write('F')
                movein(gameboard)
            elif i == 13:
                moveout(gameboard)
                gameboard.write('G')
                movein(gameboard)
            elif i == 15:
                moveout(gameboard)
                gameboard.write('H')
                movein(gameboard)
            elif i == 17:
                moveout(gameboard)
                gameboard.write('I')
                movein(gameboard)
            elif i == 19:
                moveout(gameboard)
                gameboard.write('J')
                movein(gameboard)
            elif i == 21:
                moveout(gameboard)
                gameboard.write('K')
                movein(gameboard)
            elif i == 23:
                moveout(gameboard)
                gameboard.write('L')
                movein(gameboard)
            elif i == 25:
                moveout(gameboard)
                gameboard.write('M')
                movein(gameboard)
            elif i == 27:
                moveout(gameboard)
                gameboard.write('N')
                movein(gameboard)
            elif i == 29:
                moveout(gameboard)
                gameboard.write('O')
                movein(gameboard)
            elif i == 31:
                moveout(gameboard)
                gameboard.write('P')
                movein(gameboard)
            elif i == 33:
                moveout(gameboard)
                gameboard.write('Q')
                movein(gameboard)
            elif i == 35:
                moveout(gameboard)
                gameboard.write('R')
                movein(gameboard)
            elif i == 37:
                moveout(gameboard)
                gameboard.write('S')
                movein(gameboard)
            elif i == 39:
                moveout(gameboard)
                gameboard.write('T')
                movein(gameboard)
            elif i == 41:
                moveout(gameboard)
                gameboard.write('U')
                movein(gameboard)
            elif i == 43:
                moveout(gameboard)
                gameboard.write('V')
                movein(gameboard)
            elif i == 45:
                moveout(gameboard)
                gameboard.write('W')
                movein(gameboard)
            elif i == 47:
                moveout(gameboard)
                gameboard.write('X')
                movein(gameboard)
            elif i == 49:
                moveout(gameboard)
                gameboard.write('Y')
                movein(gameboard)
            elif i == 51:
                moveout(gameboard)
                gameboard.write('Z')
                movein(gameboard)
    gameboard.penup()
    gameboard.goto(1000, 1000)
    turtle.bgcolor('tan')  # custom background
    turtle.update()
    return


def drawgridspace(gameboard):
    """
    This function draws a single gridspace on turtle graphics
    :param gameboard: it takes the parameter gameboard which is the turtle gameboard name (globalized in drawgame() func)
    :return:returns nothing, adds to gameboard
    """
    gameboard.fillcolor('saddle brown')
    gameboard.begin_fill()
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.end_fill()
    gameboard.penup()
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.pendown()
    return


def drawemptyspacevert(gameboard):
    """
    This function draws a empty vertical blockade space on the gameboard turtle graphics
    :param gameboard: takes gameboard turtle graphics
    :return: returns nothing, alters gamebaord by adding empty space
    """
    # instead of drawing a invisible rectange box, i just skipped over the width of the blockade
    gameboard.penup()
    gameboard.forward(5)
    gameboard.pendown()
    return


def drawplayeronepin(gameboard):
    """
    This function draws player one's pin on the turtle gameboard
    :param gameboard: takes the current turtle gameboard
    :return: returns nothing and updates turtle gameboard
    """
    gameboard.pendown()
    gameboard.fillcolor('saddle brown')
    gameboard.begin_fill()
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.end_fill()
    gameboard.penup()
    gameboard.right(90)
    gameboard.forward(10)
    gameboard.fillcolor('blue')
    gameboard.begin_fill()
    gameboard.left(180)
    gameboard.circle(10)
    gameboard.end_fill()
    gameboard.left(180)
    gameboard.forward(10)
    gameboard.pendown()
    return


def drawplayertwopin(gameboard):
    """
    This function draws player twos pin on the gameboard and returns thr updates gameboard for turtle graphics
    :param gameboard: takes current gameboard
    :return: returns the updated gamebaord with player twos pin
    """
    gameboard.pendown()
    gameboard.fillcolor('saddle brown')
    gameboard.begin_fill()
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.end_fill()
    gameboard.penup()
    gameboard.right(90)
    gameboard.forward(10)
    gameboard.fillcolor('red')
    gameboard.begin_fill()
    gameboard.left(180)
    gameboard.circle(10)
    gameboard.end_fill()
    gameboard.left(180)
    gameboard.forward(10)
    gameboard.pendown()
    return


def drawblockadevert(gameboard):
    """
    This function draws a blockade in the space where a vertical blockade would be on the matrix (cola)
    :param gameboard: takes current gameboard turtle graphic
    :return: updated version of gameboard turtle graphic
    """
    gameboard.fillcolor('black')
    gameboard.begin_fill()
    gameboard.forward(5)
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.forward(5)
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.penup()
    gameboard.forward(5)
    gameboard.pendown()
    gameboard.end_fill()
    return


def resetturtleeven(gameboard):
    """
    This function takes the turtle cursor and returns it to the next row on the other side of the board, like reading a book, it takes your eye from the far right to the next line on the left.
    This function is only used when going from grid space down to blockade spaces
    :param gameboard: takes current gameboard
    :return: returns updated gameboard
    """
    # grid space is always 20x20 and vertspace is always 5x20
    gameboard.penup()
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.right(90)
    for i in range(len(cola[0])):
        if i % 2 == 0:  # even (0, 2, 4, 6, 8, etc...) means it is a gridspace is has length 20
            gameboard.forward(20)
        else:  # odd (1, 3, 5, 7, etc...)
            gameboard.forward(5)
    gameboard.right(180)
    gameboard.pendown()
    return


def drawemptyspacehor(gameboard):
    """
    This function draws empty horizontal blockade space
    :param gameboard: takes current gameboard
    :return: returns updates gameboard
    """
    gameboard.penup()
    gameboard.forward(20)
    gameboard.pendown()
    return


def drawintersectingemptyspace(gameboard):
    """
    This function draws the intersections space between the 4 blockade spaces (2 vertical, 2 horizontal)
    :param gameboard: takes current gameboard
    :return: updated gameboard
    """
    gameboard.penup()
    gameboard.forward(5)
    gameboard.pendown()
    return


def drawhorizontalblockade(gameboard):
    """
    This function draws a horizontal blockade, and fills with color black
    :param gameboard: Takes current gameboard
    :return: returns updated gameboard
    """
    gameboard.fillcolor('black')
    gameboard.begin_fill()
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.forward(5)
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.right(90)
    gameboard.forward(5)
    gameboard.penup()
    gameboard.right(90)
    gameboard.forward(20)
    gameboard.pendown()
    gameboard.end_fill()
    return


def drawintersectingblockade(gameboard):
    """
    This function draws the black intersection space, and fills it if blockades are on either side or top and bottom
    :param gameboard: takes current gameboard
    :return: returns updates gameboard
    """
    gameboard.fillcolor('black')
    gameboard.begin_fill()
    gameboard.forward(5)
    gameboard.right(90)
    gameboard.forward(5)
    gameboard.right(90)
    gameboard.forward(5)
    gameboard.right(90)
    gameboard.forward(5)
    gameboard.penup()
    gameboard.right(90)
    gameboard.forward(5)
    gameboard.pendown()
    gameboard.end_fill()
    return


def resetturtleodd(gameboard):
    """
    This function takes the turtle cursor and returns it to the next row on the other side of the board, like reading a book, it takes your eye from the far right to the next line on the left.
    This function is only used when going from grid space down to blockade spaces
    :param gameboard: takes current gameboard
    :return: returns updated gameboard
    """
    # grid space is always 20x20 and vertspace is always 5x20
    gameboard.penup()
    gameboard.right(90)
    gameboard.forward(5)
    gameboard.right(90)
    for i in range(len(cola[0])):
        if i % 2 == 0:  # even (0, 2, 4, 6, 8, etc...) means it is a gridspace is has length 20
            gameboard.forward(20)
        else:  # odd (1, 3, 5, 7, etc...)
            gameboard.forward(5)
    gameboard.right(180)
    gameboard.pendown()
    return


def movetotextBIG(gameboard):
    """
    This function goes to where you would add a letter assignment to the board at the end of each row (this one is for grid spaces, thus only BIG letters (ABC))
    :param gameboard: takes current gameboard
    :return: returns updates gameboard
    """
    gameboard.penup()
    gameboard.forward(10)
    gameboard.right(90)
    gameboard.forward(15)
    return

def moveawayfromtextBIG(gameboard):
    """
    This function  goes away from where the BIG letter was just added
    :param gameboard: takes current gameboard
    :return: returns updates gameboard
    """
    gameboard.right(180)
    gameboard.forward(15)
    gameboard.left(90)
    gameboard.forward(10)
    gameboard.right(180)
    gameboard.pendown()
    return

def tolastrowtextBIG(gameboard):
    """
    This function goes to last row then to letter assignment position to add BIG letter assignment
    :param gameboard: takes current gameboard
    :return: returns updated gameboard
    """
    gameboard.penup()
    gameboard.right(90)
    gameboard.forward(25)
    gameboard.left(90)
    gameboard.forward(10)
    gameboard.right(90)
    gameboard.forward(15)
    return

def fromlastrowtextBIG(gameboard):
    """
    This function goes from letter assingmentposition to last row to original position
    :param gameboard: takes current gameboard
    :return: returns updates gameboard
    """
    gameboard.right(180)
    gameboard.forward(15)
    gameboard.left(90)
    gameboard.forward(10)
    gameboard.right(90)
    gameboard.forward(25)
    gameboard.right(90)
    gameboard.pendown()
    return

def move2text(gameboard):
    """
    This function moves cursor to where you place letter assignments (ones for blockades) on bottom of gameboard
    :param gameboard: takes current gameboard
    :return: returns updates gameboard
    """
    gameboard.forward(25)
    return

def movetotextLITTLE(gameboard):
    """
    This function moves forward to next space to place BIG letter assignments
    :param gameboard:
    :return:
    """
    gameboard.penup()
    gameboard.right(90)
    gameboard.forward(8)
    gameboard.left(90)
    gameboard.forward(5)
    return

def movefromtextLITTLE(gameboard):
    """
    This function goes away from last text placement (movetotextLITTLE)
    :param gameboard: takes current gameboard
    :return: returns updates gameboard
    """
    gameboard.left(180)
    gameboard.forward(5)
    gameboard.right(90)
    gameboard.forward(8)
    gameboard.right(90)
    gameboard.pendown()
    return

def moveout(gameboard):
    """
    This function moves to position for LITTLE letter assingments on bottom of gameboard
    :param gameboard: takes current gameboard
    :return: returns updates gameboard
    """
    gameboard.forward(13)
    gameboard.right(90)
    gameboard.forward(7)
    return

def movein(gameboard):
    """
    This function move away from little letter placement on bottom of gameboard
    :param gameboard: takes current gameboard
    :return: returns updated gameboard
    """
    gameboard.right(180)
    gameboard.forward(7)
    gameboard.left(90)
    gameboard.forward(13)
    gameboard.left(180)
    return



drawgame(cola)
gameboard.clear()

# this is loop that entire game runs in
while 1 == 1:  # this can probably be changed, something while 'value' == True and once value is false game ends/ if that's the case, make sure break statement that was originally ending the game is gone
    playersturn(1)
    drawgame(cola)
    gameboard.clear()  # i clear the board to redraw it each time a player moves, thus updating the board visually
    playersturn(2)
    drawgame(cola)
    gameboard.clear()
