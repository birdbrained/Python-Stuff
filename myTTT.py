'''
@author: Matthew Kataryniak
=========================================================
This is a playable Tic-Tac-Toe game. You have the option
of playing a 2-player game, or a single-player game
against the AI. When playing against the AI, you can
select easy or hard difficulty. Easy is just a random
number generator, but hard AI is unbeatable.

With that being said, try to beat it ;)
'''

from turtle import *
from random import randint

'''
        |        |
  -150  |  0     |   150
  150   |  150   |   150
---------------------------
        |        |
  -150  |  0     |   150
  0     |  0     |   0
---------------------------
        |        |
  -150  |  0     |   150
  -150  |  -150  |   -150
'''
        
boardT = Turtle()
boardT.width(5)
boardT.ht()
boardT.speed(0.5)
xT = Turtle()
xT.color('red')
xT.width(3)
xT.speed(0.5)
xT.pu()
oT = Turtle()
oT.color('blue')
oT.width(3)
oT.speed(0.5)
oT.pu()
winT = Turtle()
winT.color('purple')
winT.width(15)
winT.pu()
numT = Turtle()

board = ['', '', '', '', '', '', '', '', '']
winningMoves = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6)]
player1Turn = True
lessSmug = ['You fucking suck.', 'Can you not beat the easiest difficulty?!?',
            'Wow.', "Your sperm/eggs/something else important isn't important."]
smug = ['Ha, I win you scrub!', 'A chicken told me what to do.',
        "C'mon man, it's just tic-tac-toe ;D", ':3 GET REKT :3', 'I win! HAHA!',
        'Like taking candy from a blind, deaf baby.', '|_()53R',
        'wh47 73H pHuXoR D1D joO ju57 54y 7O m3h joo l177L3 B17ch?']

def drawBoard(t, cellsize):
    t.pu()
    t.bk(cellsize/2)
    t.lt(90)
    t.bk(cellsize*1.5)
    for i in range(2):
        for i in range(2):
            t.pd()
            t.fd(cellsize*3)
            t.rt(90)
            t.pu()
            t.fd(cellsize)
            t.rt(90)
        t.pu()
        t.fd(cellsize*2)
        t.rt(90)
        t.bk(cellsize)
    numT.speed(0)
    numT.pu()
    #0
    numT.goto(-150, 150-75/2)
    numT.pd()
    numT.circle(cellsize/4)
    #1
    numT.pu()
    numT.goto(0, 150-75/2)
    numT.pd()
    numT.goto(0, 150+75/2)
    #2
    numT.pu()
    numT.goto(125, 190)
    numT.rt(180)
    numT.pd()
    numT.circle(cellsize/3, -180)
    numT.setheading(0)
    numT.fd(cellsize/2)
    #3
    numT.pu()
    numT.goto(-170, 50)
    numT.lt(180)
    numT.pd()
    numT.circle(cellsize/6, -180)
    numT.setheading(180)
    numT.circle(cellsize/6, -180)
    numT.setheading(90)
    #4
    numT.pu()
    numT.goto(0, -50)
    numT.pd()
    numT.fd(cellsize/2+10)
    numT.rt(30)
    numT.bk(cellsize/3)
    numT.setheading(0)
    numT.fd(cellsize/2-30)
    #5
    numT.pu()
    numT.goto(175, 50)
    numT.pd()
    numT.bk(cellsize/3)
    numT.rt(90)
    numT.fd(cellsize/4)
    numT.rt(90)
    numT.circle(cellsize/6, -180)
    #6
    numT.pu()
    numT.goto(-140, -110)
    numT.pd()
    numT.setheading(180)
    numT.circle(cellsize/3, 180)
    numT.circle(cellsize/6, 270)
    #7
    numT.pu()
    numT.goto(-25, -110)
    numT.pd()
    numT.setheading(0)
    numT.fd(cellsize/3)
    numT.lt(60)
    numT.bk(cellsize/1.5)
    #8
    numT.pu()
    numT.goto(150, -150)
    numT.setheading(0)
    numT.pd()
    numT.circle(cellsize/5)
    numT.lt(180)
    numT.circle(cellsize/5)
    numT.pu()
    numT.back(700)   

def drawX(t, cellsize, x, y):
    t.pu()
    t.goto(x, y)
    t.setheading(0)
    t.pd()
    t.lt(45)
    length = cellsize/2.5
    for i in range(4):
        t.fd(length)
        t.bk(length)
        t.lt(90)
    t.rt(45)
    t.pu()

def drawO(t, cellsize, x, y):
    t.pu()
    t.goto(x, y)
    t.setheading(0)
    t.right(90)
    t.fd(cellsize/3)
    t.left(90)
    t.pd()
    t.circle(cellsize/3)
    t.pu()
    t.lt(90)
    t.fd(cellsize/3)
    t.right(90)

def drawShape(cellsize, x, y, player):
    if player == 'X':
        drawX(xT, cellsize, x, y)
    else:
        drawO(oT, cellsize, x, y)

def drawWinLine(x1, y1, x2, y2):
    winT.pu()
    winT.goto(x1, y1)
    winT.pd()
    winT.goto(x2, y2)
    winT.pu()

def getPlayerNames():
    return ('X', 'O')

def getMove(space, player):
    if space == 0:
        drawShape(150, -150, 150, player)
    elif space == 1:
        drawShape(150, 0, 150, player)
    elif space == 2:
        drawShape(150, 150, 150, player)
    elif space == 3:
        drawShape(150, -150, 0, player)        
    elif space == 4:
        drawShape(150, 0, 0, player)            
    elif space == 5:
        drawShape(150, 150, 0, player)            
    elif space == 6:
        drawShape(150, -150, -150, player)        
    elif space == 7:
        drawShape(150, 0, -150, player)
    elif space == 8:
        drawShape(150, 150, -150, player)

def AI_start():
    while True:
        rambo = randint(0,8)
        if rambo % 2 == 0:
            return rambo

def AI_pickWin():
    for combo in winningMoves:
        numMoves = 0
        spotsTaken = []
        for spot in combo:
            if board[spot] == 'X':
                numMoves += 1
                spotsTaken.append(spot)
        if numMoves == 2:
            for spot in combo:
                if board[spot] == '':
                    return spot
    return -1

def AI_block():
    spotToTake = -1
    for combo in winningMoves:
        numMoves = 0
        spotsTaken = []
        three = []
        for spot in combo:
            three.append(board[spot])
        if three.count('O') == 2:
            for spot in combo:
                if board[spot] == '':
                    return spot
        if three.count('O') == 1:
            for spot in combo:
                if board[spot] == '':
                    spotToTake = spot
    return spotToTake

def AI_random():
    return randint(0,8)

'''
        |        |
  0     |  1     |   2
        |        |   
---------------------------
        |        |
  3     |  4     |   5
        |        |   
---------------------------
        |        |
  6     |  7     |   8
        |        |   
'''

def checkWin():
    winner = ''
    if board[0] == board[1] == board[2] != '':
        print('='*50, '\nPLAYER', board[0], 'WINS!!!')
        drawWinLine(-175, 150, 175, 150)
        winner = board[0]
    if board[3] == board[4] == board[5] != '':
        print('='*50, '\nPLAYER', board[3], 'WINS!!!')
        drawWinLine(-175, 0, 175, 0)
        winner = board[3]
    if board[6] == board[7] == board[8] != '':
        print('='*50, '\nPLAYER', board[6], 'WINS!!!')
        drawWinLine(-175, -150, 175, -150)
        winner = board[6]
    if board[0] == board[3] == board[6] != '':
        print('='*50, '\nPLAYER', board[0], 'WINS!!!')
        drawWinLine(-150, 175, -150, -175)
        winner = board[0]
    if board[1] == board[4] == board[7] != '':
        print('='*50, '\nPLAYER', board[1], 'WINS!!!')
        drawWinLine(0, 175, 0, -175)
        winner = board[1]
    if board[2] == board[5] == board[8] != '':
        print('='*50, '\nPLAYER', board[2], 'WINS!!!')
        drawWinLine(150, 175, 150, -175)
        winner = board[2]
    if board[0] == board[4] == board[8] != '':
        print('='*50, '\nPLAYER', board[0], 'WINS!!!')
        drawWinLine(-175, 175, 175, -175)
        winner = board[0]
    if board[2] == board[4] == board[6] != '':
        print('='*50, '\nPLAYER', board[2], 'WINS!!!')
        drawWinLine(175, 175, -175, -175)
        winner = board[2]
    return winner

def playTTT():
    hasWinner = False
    players = getPlayerNames()
    drawBoard(boardT, 150)
    for player in 'XOXOXOXOX':
        print('='*50, '\n' + player + "'s turn!")
        space = 0
        while True:
            while True:
                try:
                    space = int(input('\tEnter a digit (0-8): '))
                    if space > 8 or space < 0:
                        print('\t\tIncorrect input')
                        continue
                    break
                except:
                    print('\t\tIncorrect input')
            if board[space] == '':
                board[space] = player
                break
            else:
                print('\t\tThat space is already taken.')
                continue
        #print('CURRENT BOARD:', board)
        getMove(space, player)
        winner = checkWin()
        if winner == 'X':
            hasWinner = True
            #print(winner, hasWinner)
            break
        elif winner == 'O':
            hasWinner = True
            break
        else:
            continue
    if hasWinner == False:
        print('='*50, "\nTie game...")

def playTTT_AIhard():
    player1Turn = False
    firstTurn = True
    hasWinner = False
    drawBoard(boardT, 150)
    while '' in board:
        space = 0
        player = ''
        if player1Turn:
            player = 'O'
            print('='*50, "\nHuman's turn!")
            while True:
                while True:
                    try:
                        space = int(input('\tEnter a digit (0-8): '))
                        if space > 8 or space < 0:
                            print('\t\tIncorrect input')
                            continue
                        break
                    except:
                        print('\t\tIncorrect input')
                if board[space] == '':
                    board[space] = player
                    player1Turn = not player1Turn
                    break
                else:
                    print('\t\tThat space is already taken.')
                    continue
        else:
            player = 'X'
            print('='*50, "\nK0MPU+A|-|'s turn!")
            if firstTurn:
                space = AI_start()
                firstTurn = False
            else:
                while True:
                    space = AI_pickWin()
                    if space == -1:
                        space = AI_block()
                        if space == -1:
                            space = AI_random()
                    if board[space] == '':
                        break
                    else:
                        continue
            print('\tK0MPU+A|-| picks:', space)
            board[space] = player
            player1Turn = not player1Turn
        getMove(space, player)
        winner = checkWin()
        if winner == 'X':
            hasWinner = True
            print('The K0MPU+A|-| says:')
            rando = randint(0, len(smug)-1)
            print('\t' + smug[rando])
            break
        elif winner == 'O':
            hasWinner = True
            break
        else:
            continue
    if hasWinner == False:
        print('='*50, "\nTie game...")
                
                
                
    

# The AI is X, player is O
def playTTT_AI():
    player1Turn = False
    hasWinner = False
    drawBoard(boardT, 150)
    while '' in board:
        space = 0
        player = ''
        if player1Turn:
            player = 'O'
            print('='*50, "\nHuman's turn!")
            while True:
                while True:
                    try:
                        space = int(input('\tEnter a digit (0-8): '))
                        if space > 8 or space < 0:
                            print('\t\tIncorrect input')
                            continue
                        break
                    except:
                        print('\t\tIncorrect input')
                if board[space] == '':
                    board[space] = player
                    player1Turn = not player1Turn
                    break
                else:
                    print('\t\tThat space is already taken.')
                    continue
        else:
            player = 'X'
            print('='*50, "\nComputer's turn!")
            while True:
                space = AI_random()
                print('\tComputer picks:', space)
                if board[space] == '':
                    board[space] = player
                    player1Turn = not player1Turn
                    break
                else:
                    print('\t\tThat space is already taken.')
                    continue
        getMove(space, player)
        winner = checkWin()
        if winner == 'X':
            hasWinner = True
            print('The Computer says:')
            rando = randint(0, len(lessSmug)-1)
            print('\t' + lessSmug[rando])
            break
        elif winner == 'O':
            hasWinner = True
            break
        else:
            continue
    if hasWinner == False:
        print('='*50, "\nTie game...")

#playing = 'y'            
while True:
    withAI = input('Are you playing with 2 people or against the AI?: ')
    if withAI == '2' or withAI.upper() == '2P' or withAI.upper() == '2 PEOPLE' or withAI.upper() == '2 PLAYER':
        print('Starting 2-player game...')
        playTTT()
    else:
        while True:
            withAI = input('Select a difficulty (easy / hard): ')
            if withAI.lower() == 'easy' or withAI.lower() == 'e':
                print('Starting vs easy CPU game...')
                playTTT_AI()
                break
            elif withAI.lower() == 'hard' or withAI.lower() == 'h' or withAI.upper() == 'CRAZY':
                print('Starting vs hard CPU game...good luck man...')
                playTTT_AIhard()
                break
            else:
                print('Please enter a valid difficulty.')
    playing = input('Do you want to play again? (y/n): ')
    if playing.lower() == 'yes' or playing.lower() == 'y':
        board = ['', '', '', '', '', '', '', '', '']
        player1Turn = True
        boardT.clear()
        boardT.up()
        boardT.home()
        numT.clear()
        numT.up()
        numT.home()
        xT.clear()
        xT.up()
        xT.home()
        oT.clear()
        oT.up()
        oT.home()
        winT.clear()
        winT.up()
        winT.home()
    else:
        print('Exiting game...')
        break
        
    
#drawBoard(boardT, 150)
