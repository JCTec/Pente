import pygame
from move import move
from pygame.locals import *
import sys
import copy
import timeit
import random
from AI import PenteAI
import threading
from Deepcopy import *
from Stack import Stack
from GameState import GameState
from Copy import deepCopy

class Pente(object):

    __x__ = [10, 40, 70, 100, 130, 160, 190, 220, 250, 280, 310, 340, 370, 400, 430, 460, 490, 520, 550, 1000]
    __y__ = [10, 40, 70, 100, 130, 160, 190, 220, 250, 280, 310, 340, 370, 400, 430, 460, 490, 520, 550, 1000]

    __n__ = 19

    __greenPoints__ = 0
    __bluePoints__ = 0

    __turn__ = None

    __prevMove__ = None
    __prevState__ = None

    __width__, __height__ = 750, 680

    __boardImage__ = None
    __blue__ = None
    __green__ = None

    __screen__ = None

    __board__ = None

    __selectedX__ = 0

    __selectedY__ = 0

    __background_colour__ = (224, 195, 112)

    __blueTile__ = None
    __greenTile__ = None

    __button__ = None

    __horizontal__ = None
    __vertical__ = None

    __box__ = None

    __computerBrain__ = None

    __undo__ = None

    __moveCount__ = 1

    __gameMoves__ = Stack()

    __font__ = None

    __first__ = True

    __finished__ = False

    __tik__ = timeit.default_timer()

    __isMainMenu__ = True

    __isWinnerView__ = False

    def __init__(self):
        boardImage = pygame.image.load("Pieces/penteBoard.png")

        blue = pygame.image.load("Pieces/blueGlassPiece.png")
        green = pygame.image.load("Pieces/greenGlassPiece.png")

        self.undo = pygame.image.load("Pieces/undo.png")

        self.box = pygame.image.load("Pieces/Cuadrado.png")

        self.boardImage = boardImage
        self.blue = blue
        self.green = green

        self.selectedX = 9
        self.selectedY = 9
        self.moveCount = 1

        self.turn = 'blue'

        self.blueTile = '1'
        self.greenTile = '0'

        self.computerBrain = PenteAI(self.n)

        pygame.init()
        pygame.font.init()

        self.font = pygame.font.SysFont('Comic Sans MS', 20)

        self.button = pygame.Rect(630, 15, 100, 50)

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.board = self.getNewBoard()

        self.makeBoard()


    @property
    def n(self):
        return self.__n__

    @property
    def finished(self):
        return self.__finished__

    @property
    def isMainMenu(self):
        return self.__isMainMenu__

    @property
    def isWinnerView(self):
        return self.__isWinnerView__

    @property
    def first(self):
        return self.__first__

    @property
    def tik(self):
        return self.__tik__

    @property
    def font(self):
        return self.__font__

    @property
    def gameMoves(self):
        return self.__gameMoves__

    @property
    def moveCount(self):
        return self.__moveCount__

    @property
    def horizontal(self):
        return self.__horizontal__

    @property
    def vertical(self):
        return self.__vertical__

    @property
    def selectedX(self):
        return self.__selectedX__

    @property
    def selectedY(self):
        return self.__selectedY__

    @property
    def box(self):
        return self.__box__

    @property
    def undo(self):
        return self.__undo__

    @property
    def button(self):
        return self.__button__

    @property
    def turn(self):
        return self.__turn__

    @property
    def greenTile(self):
        return self.__greenTile__

    @property
    def blueTile(self):
        return self.__blueTile__

    @property
    def prevMove(self):
        return self.__prevMove__

    @property
    def prevState(self):
        return self.__prevState__

    @property
    def greenPoints(self):
        return self.__greenPoints__

    @property
    def bluePoints(self):
        return self.__bluePoints__

    @property
    def x(self):
        return self.__x__

    @property
    def y(self):
        return self.__y__

    @property
    def width(self):
        return self.__width__

    @property
    def height(self):
        return self.__height__

    @property
    def boardImage(self):
        return self.__boardImage__

    @property
    def blue(self):
        return self.__blue__

    @property
    def green(self):
        return self.__green__

    @property
    def screen(self):
        return self.__screen__

    @property
    def background_colour(self):
        return self.__background_colour__

    @property
    def board(self):
        return self.__board__

    @property
    def computerBrain(self):
        return self.__computerBrain__

    @computerBrain.setter
    def computerBrain(self, value):
        self.__computerBrain__ = value

    @board.setter
    def board(self, value):
        self.__board__ = value

    @button.setter
    def button(self, value):
        self.__button__ = value

    @undo.setter
    def undo(self, value):
        self.__undo__ = value

    @x.setter
    def x(self, value):
        self.__x__ = value

    @prevMove.setter
    def prevMove(self, value):
        self.__prevMove__ = value

    @prevState.setter
    def prevState(self, value):
        self.__prevState__ = value

    @y.setter
    def y(self, value):
        self.__y__ = value

    @width.setter
    def width(self, value):
        self.__width__ = value

    @height.setter
    def height(self, value):
        self.__height__ = value

    @boardImage.setter
    def boardImage(self, value):
        self.__boardImage__ = value

    @blue.setter
    def blue(self, value):
        self.__blue__ = value

    @green.setter
    def green(self, value):
        self.__green__ = value

    @tik.setter
    def tik(self, value):
        self.__tik__ = value

    @screen.setter
    def screen(self, value):
        self.__screen__ = value

    @background_colour.setter
    def background_colour(self, value):
        self.__background_colour__ = value

    @greenPoints.setter
    def greenPoints(self, value):
        self.__greenPoints__ = value

    @bluePoints.setter
    def bluePoints(self, value):
        self.__bluePoints__ = value

    @turn.setter
    def turn(self, value):
        self.__turn__ = value

    @greenTile.setter
    def greenTile(self, value):
        self.__greenTile__ = value

    @blueTile.setter
    def blueTile(self, value):
        self.__blueTile__ = value

    @horizontal.setter
    def horizontal(self, value):
        self.__horizontal__ = value

    @vertical.setter
    def vertical(self, value):
        self.__vertical__ = value

    @box.setter
    def box(self, value):
        self.__box__ = value

    @selectedX.setter
    def selectedX(self, value):
        self.__selectedX__ = value

    @selectedY.setter
    def selectedY(self, value):
        self.__selectedY__ = value

    @moveCount.setter
    def moveCount(self, value):
        self.__moveCount__ = value

    @gameMoves.setter
    def gameMoves(self, value):
        self.__gameMoves__ = value

    @font.setter
    def font(self, value):
        self.__font__ = value

    @first.setter
    def first(self, value):
        self.__first__ = value

    @finished.setter
    def finished(self, value):
        self.__finnished__ = value

    @isMainMenu.setter
    def isMainMenu(self, value):
        self.__isMainMenu__ = value

    @isWinnerView.setter
    def isWinnerView(self, value):
        self.__isWinnerView__ = value


    def __makeBoard__(self, board, turn):
        self.screen.fill(self.background_colour)

        self.screen.blit(self.boardImage, (30, 30))

        for row in range(self.n):

            for col in range(self.n):
                if board[row][col] == '1':
                    self.screen.blit(self.blue, (self.x[row], self.y[col]))

                elif board[row][col] == '0':
                    self.screen.blit(self.green, (self.x[row], self.y[col]))

        textsurface = self.font.render('Turno:', False, (0, 0, 0))

        self.screen.blit(textsurface, (self.width - 275, self.height - 95))
        if turn == 'blue':
            self.screen.blit(self.blue, (self.width - 215, self.height - 100))
        else:
            self.screen.blit(self.green, (self.width - 215, self.height - 100))

        if self.greenPoints == 1:
            self.screen.blit(self.green, (20, self.height - 85))
        elif self.greenPoints == 2:
            self.screen.blit(self.green, (20, self.height - 85))
            self.screen.blit(self.green, (60, self.height - 85))
        elif self.greenPoints == 3:
            self.screen.blit(self.green, (20, self.height - 85))
            self.screen.blit(self.green, (60, self.height - 85))
            self.screen.blit(self.green, (100, self.height - 85))
        elif self.greenPoints == 4:
            self.screen.blit(self.green, (20, self.height - 85))
            self.screen.blit(self.green, (60, self.height - 85))
            self.screen.blit(self.green, (100, self.height - 85))
            self.screen.blit(self.green, (140, self.height - 85))

        if self.bluePoints == 1:
            self.screen.blit(self.blue, (20, self.height - 40))
        elif self.bluePoints == 2:
            self.screen.blit(self.blue, (20, self.height - 40))
            self.screen.blit(self.blue, (60, self.height - 40))
        elif self.bluePoints == 3:
            self.screen.blit(self.blue, (20, self.height - 40))
            self.screen.blit(self.blue, (60, self.height - 40))
            self.screen.blit(self.blue, (100, self.height - 40))
        elif self.bluePoints == 4:
            self.screen.blit(self.blue, (20, self.height - 40))
            self.screen.blit(self.blue, (60, self.height - 40))
            self.screen.blit(self.blue, (100, self.height - 40))
            self.screen.blit(self.blue, (140, self.height - 40))

        self.screen.blit(self.undo, self.button)

        self.screen.blit(self.box, (self.x[self.selectedY]+7, self.y[self.selectedX]+7))

        textsurface = self.font.render('Jugadas', False, (0, 0, 0))

        self.screen.blit(textsurface, (600,80))

        gameMoveSS = copy.deepcopy(self.gameMoves)

        xText = self.font.render('X: ', False, (0, 0, 0))
        yText = self.font.render('Y: ', False, (0, 0, 0))

        size = gameMoveSS.size()

        if size > 14:
            size = 14

        movessss = self.moveCount

        for x in range(size):
            if not gameMoveSS.isEmpty():
                move = gameMoveSS.pop()

                movessss -= 1

                textsurface = self.font.render(str(movessss), False, (0, 0, 0))

                self.screen.blit(textsurface, (580, (115 + (x*40))))

                if move.tile == '1':
                    self.screen.blit(self.blue, (600, (110 + (x*40))))
                else:
                    self.screen.blit(self.green, (600, (110 + (x*40))))

                myX = self.font.render(str(move.x), False, (0, 0, 0))
                myY = self.font.render(str(move.y), False, (0, 0, 0))

                self.screen.blit(xText, (650, (115 + (x*40))))
                self.screen.blit(myX, (670, (115 + (x*40))))
                self.screen.blit(yText, (710, (115 + (x*40))))
                self.screen.blit(myY, (730, (115 + (x*40))))

        pygame.display.flip()


    def makeBoard(self):
        if self.isMainMenu:
            self.mainMenu()
        else:
            t = threading.Thread(target=self.__makeBoard__, args=(deepcopy(self.board), self.turn))

            t.start()

    def getNewBoard(self):
        NB = []
        Row = []

        for i in range(self.n):
            Row.append('.')

        for j in range(self.n):
            NB.append(deepcopy(Row))

        return NB

    def isValidMove(self, move):

        ##if (move.x >= 0 and move.x < self.n and move.y >= 0 and move.y < self.n):

        if (move.x != -1 and move.y != -1 and move.x != 1000 and move.y != 1000):
            return (self.board[move.x][move.y] == '.')
        return False

    def isCaptureMove(self, jugador, move):
        ##check to see if the move made is going to capture
        ccount = 0
        if jugador == '0':
            contrincante = '1'
        else:
            contrincante = '0'

        ##check horizontal captures
        if (move.y > 2 and self.board[move.x][move.y - 1] == contrincante and self.board[move.x][move.y - 2] == contrincante and self.board[move.x][move.y - 3] == jugador):
            self.board[move.x][move.y - 1] = '.'
            self.board[move.x][move.y - 2] = '.'
            ccount += 1

        if (move.y < self.n - 3 and self.board[move.x][move.y + 1] == contrincante and self.board[move.x][move.y + 2] == contrincante and self.board[move.x][move.y + 3] == jugador):
            self.board[move.x][move.y + 1] = '.'
            self.board[move.x][move.y + 2] = '.'
            ccount += 1

        ##check vertical captures
        if (move.x > 2 and self.board[move.x - 1][move.y] == contrincante and self.board[move.x - 2][move.y] == contrincante and self.board[move.x - 3][move.y] == jugador):
            self.board[move.x - 1][move.y] = '.'
            self.board[move.x - 2][move.y] = '.'
            ccount += 1

        if (move.x < self.n - 3 and self.board[move.x + 1][move.y] == contrincante and self.board[move.x + 2][move.y] == contrincante and self.board[move.x + 3][move.y] == jugador):
            self.board[move.x + 1][move.y] = '.'
            self.board[move.x + 2][move.y] = '.'
            ccount += 1

        ##check diagonal cpatures
        if (move.x > 2 and move.y > 2 and self.board[move.x - 1][move.y - 1] == contrincante and self.board[move.x - 2][move.y - 2] == contrincante and self.board[move.x - 3][move.y - 3] == jugador):
            self.board[move.x - 1][move.y - 1] = '.'
            self.board[move.x - 2][move.y - 2] = '.'
            ccount += 1

        if (move.x < self.n - 3 and move.y < self.n - 3 and self.board[move.x + 1][move.y + 1] == contrincante and self.board[move.x + 2][move.y + 2] == contrincante and self.board[move.x + 3][move.y + 3] == jugador):
            self.board[move.x + 1][move.y + 1] = '.'
            self.board[move.x + 2][move.y + 2] = '.'
            ccount += 1

        ##check other diagonal captures
        if (move.x > 2 and move.y < self.n - 3 and self.board[move.x - 1][move.y + 1] == contrincante and self.board[move.x - 2][move.y + 2] == contrincante and self.board[move.x - 3][move.y + 3] == jugador):
            self.board[move.x - 1][move.y + 1] = '.'
            self.board[move.x - 2][move.y + 2] = '.'
            ccount += 1

        if (move.x < self.n - 3 and move.y < self.n - 3 and self.board[move.x + 1][move.y - 1] == contrincante and self.board[move.x + 2][move.y - 2] == contrincante and self.board[move.x + 3][move.y - 3] == jugador):
            self.board[move.x + 1][move.y - 1] = '.'
            self.board[move.x + 2][move.y - 2] = '.'
            ccount += 1

        return ccount

    def makeMove(self, jugador, move):
        captures = self.isCaptureMove(jugador, move)
        self.board[move.x][move.y] = jugador

        if jugador == '1':
            self.computerBrain.bcaptures = self.computerBrain.bcaptures + captures
            self.greenPoints = self.greenPoints + captures
        else:
            self.computerBrain.wcaptures = self.computerBrain.wcaptures + captures
            self.bluePoints = self.bluePoints + captures


    def isBoardFull(self):
        rango = range(self.n)

        for row in rango:
            for col in rango:
                if self.board[row][col] == '.':
                    return False
        return True

    def isWinner(self, tile):

        rango4 = range(self.n - 4)
        rango = range(self.n)

        ##checking horizontal spaces
        for y in rango:
            for x in rango4:
                if self.board[x][y] == tile and self.board[x + 1][y] == tile and self.board[x + 2][y] == tile and self.board[x + 3][y] == tile and self.board[x + 4][y] == tile:
                    return True

        ##checking for vertical spaces
        for x in rango:
            for y in rango4:
                if self.board[x][y] == tile and self.board[x][y + 1] == tile and self.board[x][y + 2] == tile and self.board[x][y + 3] == tile and self.board[x][y + 4] == tile:
                    return True

        ##checking for diagonal spaces
        for x in rango4:
            for y in range(4, self.n):
                if self.board[x][y] == tile and self.board[x + 1][y - 1] == tile and self.board[x + 2][y - 2] == tile and self.board[x + 3][y - 3] == tile and self.board[x + 4][y - 4] == tile:
                    return True

        ##check other diagonal spaces
        for x in rango4:
            for y in rango4:
                if self.board[x][y] == tile and self.board[x + 1][y + 1] == tile and self.board[x + 2][y + 2] == tile and self.board[x + 3][y + 3] == tile and self.board[x + 4][y + 4] == tile:
                    return True

        ##checking capture pairs
        if tile == '1':
            if self.greenPoints >= 5:
                return True
        else:
            if self.bluePoints >= 5:
                return True
        return False

    def didClickMouse(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.button.collidepoint(mouse_pos):
            # prints current location of mouse

            print("Regresando Jugada")

            self.undoMove()
        else:
            print("Click")

    def makeMyMove(self):
        winner = None

        move = self.getHumanMove()

        # check if the move is valid
        if self.isValidMove(move):
            self.makeMove(self.blueTile, move)
            self.makeBoard()

            if self.isWinner(self.blueTile):
                winner = 'blue'

            self.turn = 'green'

            if self.isBoardFull():
                winner = 'tie'

            gameState = GameState(self.board, '1', move)

            self.gameMoves.push(gameState)
            self.moveCount += 1

            self.makeBoard()

            if winner != None:
                if winner == 'tie':
                    print("There is a tie")
                    self.saveLog()
                    self.finished = True
                else:
                    if winner != None:
                        if winner == 'tie':
                            print("There is a tie")
                            self.saveLog()
                            self.finished = True
                        else:
                            if winner == 'blue':
                                print("the winner is %s" % winner)
                                self.saveLog()
                                self.isWinnerView = True
                                self.theWinnerIsBlue()
                            else:
                                print("the winner is %s" % winner)
                                self.saveLog()
                                self.isWinnerView = True
                                self.theWinnerIsGreen()
            else:
                winner = None

                movesss = self.computerBrain.getComputerMove(self.board, '0')

                move = self.tupleJoin(movesss[1])

                # check if the move is valid
                if self.isValidMove(move):
                    self.makeMove(self.greenTile, move)
                    self.makeBoard()

                    if self.isWinner(self.greenTile):
                        winner = 'green'

                    self.turn = 'blue'

                    if self.isBoardFull():
                        winner = 'tie'

                    gameState = GameState(self.board, '0', move, movesss[0])

                    self.gameMoves.push(gameState)
                    self.moveCount += 1

                    if winner != None:
                        if winner == 'tie':
                            print("There is a tie")
                            self.saveLog()
                            self.finished = True
                        else:
                            if winner == 'blue':
                                print("the winner is %s" % winner)
                                self.saveLog()
                                self.isWinnerView = True
                                self.theWinnerIsBlue()
                            else:
                                print("the winner is %s" % winner)
                                self.saveLog()
                                self.isWinnerView = True
                                self.theWinnerIsGreen()
                    else:
                        self.makeBoard()

                else:
                    print("move chosen was invalid")
                    print(move)
                    self.gameMoves.pop()
                    self.moveCount -= 1

                    self.board = deepCopy(self.gameMoves.peek().board)

                    self.makeBoard()

        else:
            print(move)
            print("move chosen was invalid")

    def didClickKey(self, event):

        if self.isWinnerView:
            if event.key == pygame.K_RETURN:
                self.isWinnerView = False
                self.isMainMenu = True

                self.makeBoard()
        else:
            if self.isMainMenu:
                if event.key == pygame.K_RETURN:
                    self.isMainMenu = False

                    self.makeBoard()
            else:
                if event.key == pygame.K_LEFT and (not self.first):
                    if self.selectedY != 0:
                        self.selectedY -= 1
                        self.makeBoard()

                elif event.key == pygame.K_RIGHT and (not self.first):
                    if self.selectedY < 18:
                        self.selectedY += 1
                        self.makeBoard()

                elif event.key == pygame.K_DOWN and (not self.first):
                    if self.selectedX < 18:
                        self.selectedX += 1
                        self.makeBoard()

                elif event.key == pygame.K_UP and (not self.first):
                    if self.selectedX != 0:
                        self.selectedX -= 1
                        self.makeBoard()

                elif event.key == pygame.K_RETURN:
                    if self.first:
                        self.first = False

                    self.makeMyMove()


    def undoMove(self):
        self.moveCount -= 2
        self.gameMoves.pop()
        self.gameMoves.pop()

        if not self.gameMoves.isEmpty():
            self.board = deepCopy(self.gameMoves.peek().board)
        else:
            self.board = self.getNewBoard()

        self.makeBoard()


    def getCoordinates(self):
        x, y = pygame.mouse.get_pos()

        print(pygame.mouse.get_pos())

        isbigger = False

        newX = -1
        newY = -1

        for xs in range(self.n):
            if not isbigger:
                if x >= (self.x[xs]):
                    newX = xs
                else:
                    isbigger = True

        isbigger = False

        for ys in range(self.n):
            if not isbigger:
                if y >= (self.y[ys]):
                    newY = ys
                else:
                    isbigger = True

        moves = move(newX, newY)
        print(moves)
        return moves

    def getHumanMove(self):
        moves = move(self.selectedY, self.selectedX)

        return moves

    def tupleJoin(self, tuple):
        return move(tuple[0],tuple[1])

    def restart(self):
        self.board = self.getNewBoard()
        self.greenPoints = 0
        self.bluePoints = 0

        self.computerBrain = None

        self.selectedX = 9
        self.selectedY = 9
        self.moveCount = 1

        self.turn = 'blue'

        self.blueTile = '1'
        self.greenTile = '0'

        self.computerBrain = PenteAI(self.n)


    def saveLog(self):

        tok = timeit.default_timer()

        file = open("dump.txt", "w")

        file.write("----------------------Pente--------------------------- \n")

        file.write("Duración de partida: " + str(tok - self.tik) + " \n")

        file.write("Jugadas: \n")

        stack = Stack()

        while not self.gameMoves.isEmpty():
            stack.push(self.gameMoves.pop())

        count = 1

        while not stack.isEmpty():
            moves = stack.pop()

            play = 'Computadora'

            if moves.tile == '1':
                play = 'Humano'

            strw = str(count) + ".- " + play + " X: " + str(moves.x) + " Y: " + str(moves.y)

            count += 1

            if moves.tile == '0':
                strw += " Valor: " + str(moves.value)

            strw += "\n"

            file.write(strw)

        file.write("------------------------------------------------------\n")

        file.close()


    def theWinnerIsBlue(self):
        __background__ = pygame.image.load("Pieces/fondo.jpg")

        background = pygame.transform.scale(__background__, (750, 680))

        self.screen.blit(background, (0, 0))

        __pentee__ = pygame.image.load("Pieces/winner_blue.png")

        pentee = pygame.transform.scale(__pentee__, (750, 680))

        self.screen.blit(pentee, (0, 0))

        textsurface = self.font.render('Preciona enter para volver al menu...', False, (0, 0, 0))

        self.screen.blit(textsurface, (275, 600))

        pygame.display.flip()

        self.restart()


    def theWinnerIsGreen(self):
        __background__ = pygame.image.load("Pieces/fondo.jpg")

        background = pygame.transform.scale(__background__, (750, 680))

        self.screen.blit(background, (0, 0))

        __pentee__ = pygame.image.load("Pieces/winner_green.png")

        pentee = pygame.transform.scale(__pentee__, (750, 680))

        self.screen.blit(pentee, (0, 0))

        textsurface = self.font.render('Preciona enter para volver al menu...', False, (0, 0, 0))

        self.screen.blit(textsurface, (275, 600))

        pygame.display.flip()

        self.restart()

    def mainMenu(self):
        __background__ = pygame.image.load("Pieces/fondo.jpg")

        background = pygame.transform.scale(__background__, (750, 680))

        self.screen.blit(background, (0,0))

        __pentee__ = pygame.image.load("Pieces/pente.png")

        pentee = pygame.transform.scale(__pentee__, (750, 680))

        self.screen.blit(pentee, (0, 0))

        textsurface = self.font.render('Preciona Enter Para Jugar...', False, (0, 0, 0))

        self.screen.blit(textsurface, (275, 600))

        pygame.display.flip()







