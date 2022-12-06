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
    if Row >= 3 and Row <= 25 and Col >= 3 and Col <= 25:
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
        return print('\n \n \n'), print('Board is too small! Try a larger board size'), print('\n \n \n'), boardsize()


def boardsize():
    """
    This functions takes no parameters and asks user for input on board size, should be first functions called in program
    :return: function returns nothing, but globalizes inputs (Row and Col)
    """
    global Col, Row
    print('----------------------Board Size----------------------\n'
          'Max size is 25x25 and smallest size is 3x3 (Row x Columns)\n'
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


def playersturn(player):
    """
    This function asks user to either move piece or place blockade and checks every conditional
    property (rule)
    :param player: Takes parameter player, to know which player's turn it is
    :return: This functions globalizes the movelocation or blockadelocation based on user
             input. Returns nothing.
    """
    global movelocation, blockadelocation
    made_choice = False
    while 1:
        print(f'---------------------------Player {player}---------------------------')
        print(f'Do you want to move your piece (M) or would you like to place a blockade (B): ', end='')
        choice = input()
        while (choice == 'M' or choice == 'm') or made_choice:
            made_choice = True
            print(
                'You may only move your piece one gridspace away from your current location, diagonals are NOT included!')
            print(f"Please specify location that you want to move (side character then bottom, EX's --> aa, ea, "
                  f"bd): ", end='')
            movelocation = input()
            if len(movelocation) != 2:
                movelocation += '00'
            checker = list(movelocation)
            if checker[0].isdigit() == False and checker[1].isdigit() == False and len(checker) == 2:
                print('')
                print('')
                CheckPieceMovedOneGridSpace(movelocation,
                                            player)  # check for conditionals before using movepiece() function to actually move he piece  and gives GameIsGood Variable
                check4pinwhenmovingpin(player)  # gives space varialble
                checkifblockadeinway(player)
                if GameIsGood and space and blockadeNotinway:
                    movepiece(movelocation, player)
                    made_choice = False
                    checkforwinner(player)
                    if winnerexists:
                        print('------------------------------------------------------')
                        print('----------------------Game Over-----------------------')
                        print('------------------------------------------------------')
                        print(f'--------------------Player {player} Won!---------------------')
                        print('------------------------------------------------------')
                        quit()
                    break
                elif not GameIsGood:
                    print('Remember! You may only move ONE grid space away from your current location.')
                    continue
                elif not space:
                    print('Sorry, but something is in the way!')
                    continue
                elif not blockadeNotinway:
                    print('Looks like someone blocked this path, try moving a different direction')
                    continue
                else:
                    print('Follow the rules! Try a new spot.')
                    print('')
                    print('')
                    continue
            else:
                print('Enter a valid move location')
        while (choice == 'B' or choice == 'b') or made_choice:
            made_choice = True
            print(
                'You may place a blockade any place you choose, as long as it is \n NOT obstructed by another blockade or traps the opposing player')
            print(f"Please specify location that you want to place a blockade (side character then bottom), \n"
                  f"EX's --> AbAa): ", end='')
            blockadelocation = input()
            blocklist = list(blockadelocation)
            if len(blockadelocation) == 4 and blocklist[0].isdigit() == False and blocklist[1].isdigit() == False and blocklist[2].isdigit() == False and blocklist[3].isdigit() == False:
                print('')
                print('')
                # check conditional that block input is within boundaries
                checkblockade(blockadelocation)
                if coastisclear == True:
                    placeblockade(blockadelocation)
                    made_choice = False
                    break
            else:
                print('The desired blockade is not possible, make sure the length is accurate')
                continue
        if not ((choice == 'B' or choice == 'b') or (choice == 'M' or choice == 'm')):
            print('Please enter a valid input.')
            continue
        break
    return

#  this is probably most used functions, as it runs it also runs just about every conditinal functions as well
#  Each player move and blockade placement is checked through other functions before being placed through this function


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
    global move
    move = list(movelocation)  # [ , ], bottom then side
    for i in range(len(move)):  # making list a set of int
        if move[i] in ColAssignments:
            move[i] = int(ColAssignments.index(move[i]))
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
        if move[i] in ColAssignments:
            move[i] = ColAssignments.index(move[i])
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
    try:
        if cola[move[0]][move[1]] == '=':
            blockadeNotinway = False
        else:
            blockadeNotinway = True
    except:
        print('Invalid move, please try something within boards limits.')
        playersturn(player)
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
            if i % 2 == 1:  # odd
                # add text/ way for assigning grid spaces/ blockade spaces a value ex- aa, AaAb, etc...
                if i >= 1:  # declaring not last row
                    movetotextBIG(gameboard)
                    gameboard.write(ColAssignments[i-1])
                    moveawayfromtextBIG(gameboard)
                if i == len(cola) - 2:  # last row
                    tolastrowtextBIG(gameboard)
                    gameboard.write(ColAssignments[i+1])
                    fromlastrowtextBIG(gameboard)
                resetturtleeven(gameboard)
            elif i % 2 == 0:  # even
                movetotextLITTLE(gameboard)
                gameboard.write(ColAssignments[i-1])
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
    for i in range(len(cola[0])-1):
        if i % 2 != 0: # even/ for gridspace assignments
            move2text(gameboard)
            gameboard.write(ColAssignments[i+1])
        elif i % 2 == 0:  # odd / blockade spaces assignments (write text)
            moveout(gameboard)
            gameboard.write(ColAssignments[i+1])
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
