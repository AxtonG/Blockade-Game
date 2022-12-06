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
        while (choice == 'B' or choice == 'b') or made_choice:
            made_choice = True
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




def movepiece(movelocation, player):
    """
    Function places player pin based on player number and movelocation
    :param movelocation: This parameter takes the input of location (2-character input from letter assignment)
    :param player: This parameter takes into account which player is actually moving
    :return: function returns nothing and gloalizes nothing, but alters the gameboard matrix (cola) and places the players pin where they decided to move.
    """
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
