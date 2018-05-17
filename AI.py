import sys
import copy
import timeit
import pickle
import os
import sys
from Node import Node
from Deepcopy import *
from Copy import *
import threading
import multiprocessing

class PenteAI(object):

    __prevMove__ = None
    __n__ = 0
    __bcaptures__ = 0
    __wcaptures__ = 0

    def __init__(self, n):
        self.prevMove = None
        self.n = n
        self.bcaptures = 0
        self.wcaptures = 0

        self.cache = Node()


    @property
    def prevMove(self):
        return self.__prevMove__

    @prevMove.setter
    def prevMove(self, value):
        self.__prevMove__ = value

    @property
    def n(self):
        return self.__n__

    @n.setter
    def n(self, value):
        self.__n__ = value

    @property
    def bcaptures(self):
        return self.__bcaptures__

    @bcaptures.setter
    def bcaptures(self, value):
        self.__bcaptures__ = value

    @property
    def wcaptures(self):
        return self.__wcaptures__

    @wcaptures.setter
    def wcaptures(self, value):
        self.__wcaptures__ = value


    def getComputerMove(self, board, tile):
        m = self.AlphaBeta(board, 2, tile)

        self.prevMove = m[1]

        #self.cache = self.generateTree(Node(0, board), board, 2,'0')

        #self.cache.print_tree(self.cache)

        return m

    def generateChildren3(self, board, player):
        cstates = []

        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
            for j in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
                if self.isValidMove(board, (i, j)):
                    cstates.append((deepCopy(board), (i, j)))
                    self.makeMove(cstates[-1][0], player, cstates[-1][1])

        return cstates

#EXPERIMENTAL
    def generateNodes(self, root, board, player):
        cstates = []

        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
            for j in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
                if self.isValidMove(board, (i, j)):

                    b = deepcopy(board)

                    m = (i, j)

                    self.makeMove(b, player, m)

                    cstates.append(Node(0, b, m, root))

        return cstates

    def generateTree(self, root, board, depth, player):
        ##figure the opposite tile
        if player == '1':
            unplayer = '0'
        else:
            unplayer = '1'

        ##return heuristic if leaf
        if depth == 0:
            if player == '1':
                return Node(0, deepCopy(board), board, root)
            else:
                return Node(0, deepCopy(board), board, root)
        ##for each children find next
        for succ in self.generateNodes(root, board, player):
            succ.addChildren(self.generateTree(succ, deepCopy(board), depth - 1, unplayer))

            root.addChildren(succ)
        return root
#------------------------------------------------------------------

    def generateChildren4(self, board, player):
        cstates = []

        cstates1 = []

        cstates2 = []

        cstates3 = []

        cstates4 = []

        t1 = threading.Thread(target=self.firstPart, args=(deepCopy(board), player, cstates1, cstates))
        t2 = threading.Thread(target=self.secondPart, args=(deepCopy(board), player, cstates2, cstates))
        t3 = threading.Thread(target=self.thirdPart, args=(deepCopy(board), player, cstates3, cstates))
        t4 = threading.Thread(target=self.fourthPart, args=(deepCopy(board), player, cstates4, cstates))

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()

        return cstates

    def firstPart(self, board, player, cstates1, cstates):
        for i in [0,1,2]:
            for j in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
                 if self.isValidMove(board, (i, j)):
                     cstates1.append((deepCopy(board), (i, j)))
                     self.makeMove(cstates1[-1][0], player, cstates1[-1][1])

        cstates += cstates1

    def secondPart(self, board, player, cstates2, cstates):
        for i in [3,4,5,6]:
            for j in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
                 if self.isValidMove(board, (i, j)):
                     cstates2.append((deepCopy(board), (i, j)))
                     self.makeMove(cstates2[-1][0], player, cstates2[-1][1])

        cstates += cstates2

    def thirdPart(self, board, player, cstates3, cstates):
        for i in [7,8,9,10,11,12]:
            for j in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
                 if self.isValidMove(board, (i, j)):
                     cstates3.append((deepCopy(board), (i, j)))
                     self.makeMove(cstates3[-1][0], player, cstates3[-1][1])

        cstates += cstates3

    def fourthPart(self, board, player, cstates4, cstates):
        for i in [13,14,15,16,17,18]:
            for j in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
                 if self.isValidMove(board, (i, j)):
                     cstates4.append((deepCopy(board), (i, j)))
                     self.makeMove(cstates4[-1][0], player, cstates4[-1][1])

        cstates += cstates4

    def AlphaBeta(self, board, depth, player):
        #self.cache = Node(0, deepCopy(board))
        tik = timeit.default_timer()
        m = self.minValue((board, -1), depth, player, (float("-inf"), -1), (float("inf"), -1))
        tok = timeit.default_timer()
        print("Tiempo de Procesamiento: ", tok - tik)

        return m



    def maxValue(self, board, depth, player, alpha, beta):
        ##figure the opposite tile
        if player == '1':
            unplayer = '0'
        else:
            unplayer = '1'

        ##return heuristic if leaf
        if depth == 0:
            if player == '1':
                return (self.heuristic(board[0]), board[1])
            else:
                return (self.heuristic(board[0]) * -1, board[1])
        ##for each children find next
        for succ in self.generateChildren4(board[0], player):
            m = self.minValue(succ, depth - 1, unplayer, alpha, beta)
            if m[0] > alpha[0]:
                alpha = m
            if alpha[0] >= beta[0]:
                return alpha
        return alpha

    def minValue(self, board, depth, player, alpha, beta):
        ##figure the opposite tile
        if player == '1':
            unplayer = '0'
        else:
            unplayer = '1'

        ##return heuristic if leaf
        if depth == 0:
            if player == '1':
                return self.heuristic(board[0]), board[1]
            else:
                return self.heuristic(board[0]) * -1, board[1]
        ##for each children find next
        for succ in self.generateChildren4(board[0], player):
            m = self.maxValue(succ, depth - 1, unplayer, alpha, beta)
            if m[0] < beta[0]:
                beta = m
            if alpha[0] >= beta[0]:
                return beta
        return beta

    ##determine the value of a state, taking advantage of capturing as many as can be to win.
    def heuristic(self, board):
        capture_count = 0
        ncapture_count = 0

        tile = '0'
        untile = '1'

        rango = range(self.n)

        # check horizontal
        for y in rango:
            for x in range(self.n - 3):
                if (board[x][y] == tile and board[x + 1][y] == untile and board[x + 2][y] == '.') or (board[x][y] == '.' and board[x + 1][y] == untile and board[x + 2][y] == tile):
                    capture_count += 1

                if (board[x][y] == tile and board[x + 1][y] == untile and board[x + 2][y] == untile) or (board[x + 1][y] == untile and board[x + 2][y] == untile and board[x + 3][y] == tile):
                    capture_count += 2

                if (board[x][y] == untile and board[x + 1][y] == tile and board[x + 2][y] == '.') or (board[x][y] == '.' and board[x + 1][y] == tile and board[x + 2][y] == untile):
                    ncapture_count += 1

                if (board[x][y] == untile and board[x + 1][y] == tile and board[x + 2][y] == tile) or (board[x + 1][y] == tile and board[x + 2][y] == tile and board[x + 3][y] == untile):
                    ncapture_count += 2

        # check vertical
        for x in rango:
            for y in range(self.n - 2):

                if y != 17 and y != 18:
                    if (board[x][y] == tile and board[x][y + 1] == untile and board[x][y + 1] == '.') or (
                            board[x][y] == '.' and board[x][y + 1] == untile and board[x][y + 1] == tile):
                        capture_count += 1

                    if (board[x][y] == tile and board[x][y + 1] == untile and board[x][y + 2] == untile) or (
                            board[x][y] == untile and board[x][y + 1] == untile and board[x][y + 2] == tile):
                        capture_count += 2

                    if (board[x][y] == untile and board[x][y + 1] == tile and board[x][y + 2] == '.') or (
                            board[x][y] == '.' and board[x][y + 1] == tile and board[x][y + 2] == untile):
                        ncapture_count += 1

                    if (board[x][y] == untile and board[x][y + 1] == tile and board[x][y + 2] == tile) or (
                            board[x][y] == tile and board[x][y + 1] == tile and board[x][y + 2] == untile):
                        ncapture_count += 2

                if x != 17 and x != 18 and y != 0 and y != 1:
                    if (board[x][y] == tile and board[x + 1][y - 1] == untile and board[x + 2][y - 2] == '.') or (
                            board[x][y] == '.' and board[x + 1][y - 1] == untile and board[x + 2][y - 2] == tile):
                        capture_count += 1

                    if (board[x][y] == tile and board[x + 1][y - 1] == untile and board[x + 2][y - 2] == untile) or (
                            board[x][y] == untile and board[x + 1][y - 1] == untile and board[x + 2][y - 2] == tile):
                        capture_count += 2

                    if (board[x][y] == untile and board[x + 1][y - 1] == tile and board[x + 2][y - 2] == '.') or (
                            board[x][y] == '.' and board[x + 1][y - 1] == tile and board[x + 2][y - 2] == untile):
                        ncapture_count += 1

                    if (board[x][y] == untile and board[x + 1][y - 1] == tile and board[x + 2][y - 2] == tile) or (
                            board[x][y] == tile and board[x + 1][y - 1] == tile and board[x + 2][y - 2] == untile):
                        ncapture_count += 2

                if x != 15 and x != 16 and x != 17 and x != 18 and y != 15 and y != 16 and y != 17 and y != 18:
                    if (board[x][y] == tile and board[x + 1][y - 1] == untile and board[x + 2][y + 2] == '.') or (
                            board[x][y] == '.' and board[x + 1][y - 1] == untile and board[x + 2][y + 2] == tile):
                        capture_count += 1

                    if (board[x][y] == tile and board[x + 1][y - 1] == untile and board[x + 2][y + 2] == untile) or (
                            board[x][y] == untile and board[x + 1][y - 1] == untile and board[x + 2][y + 2] == tile):
                        capture_count += 2

                    if (board[x][y] == untile and board[x + 1][y - 1] == tile and board[x + 2][y + 2] == '.') or (
                            board[x][y] == '.' and board[x + 1][y - 1] == tile and board[x + 2][y + 2] == untile):
                        ncapture_count += 1

                    if (board[x][y] == untile and board[x + 1][y - 1] == tile and board[x + 2][y + 2] == tile) or (
                            board[x][y] == tile and board[x + 1][y - 1] == tile and board[x + 2][y + 2] == untile):
                        ncapture_count += 2

        return capture_count - ncapture_count




    ##determine the value of a state, based on whether the next available state allows for Trias, or block Trias.
    def heuristic2(self, board):
        tria_count = 0
        ntria_count = 0

        tile = '0'
        untile = '1'

        # check horizontal spaces for 2 in a rows or block 3 in a rows
        for y in range(self.n):
            for x in range(self.n - 4):
                if (board[x][y] == '.') and (board[x + 1][y] == tile) and (board[x + 2][y] == '.'):
                    tria_count += 1

                if (board[x][y] == '.') and (board[x + 1][y] == tile) and (board[x + 2][y] == tile and board[x + 3][y] == '.'):
                    tria_count += 2

                if (board[x][y] == '.') and (board[x + 1][y] == tile) and (board[x + 2][y] == tile and board[x + 3][y] == tile) and board[x + 4][y] == '.':
                    tria_count += 3

                if (board[x][y] == '.') and (board[x + 1][y] == untile) and (board[x + 2][y] == '.'):
                    ntria_count += 1

                if (board[x][y] == '.') and (board[x + 1][y] == untile) and (board[x + 2][y] == untile and board[x + 3][y] == '.'):
                    ntria_count += 2

                if (board[x][y] == '.') and (board[x + 1][y] == untile) and (board[x + 2][y] == untile and board[x + 3][y] == untile) and board[x + 4][y] == '.':
                    ntria_count += 3

        # check vertical spaces for 2 in a rows or block 3 in a rows
        for x in range(self.n):
            for y in range(self.n - 4):
                if (board[x][y] == '.' and board[x][y + 1] == tile) and (board[x][y + 2] == '.'):
                    tria_count += 1

                if (board[x][y] == '.' and board[x][y + 1] == tile) and (board[x][y + 2] == tile and board[x][y + 3] == '.'):
                    tria_count += 2

                if (board[x][y] == '.' and board[x][y + 1] == tile) and (board[x][y + 2] == tile and board[x][y + 3] == tile) and (board[x][y + 4] == '.'):
                    tria_count += 3

                if (board[x][y] == '.' and board[x][y + 1] == untile) and (board[x][y + 2] == '.'):
                    ntria_count += 1

                if (board[x][y] == '.' and board[x][y + 1] == untile) and (board[x][y + 2] == untile and board[x][y + 3] == '.'):
                    ntria_count += 2

                if (board[x][y] == '.' and board[x][y + 1] == untile) and (board[x][y + 2] == untile and board[x][y + 3] == untile) and (board[x][y + 4] == '.'):
                    ntria_count += 3

        # check diagonal /
        for x in range(self.n - 4):
            for y in range(4, self.n):
                if (board[x][y] == '.' and board[x][y] == tile) and (board[x + 1][y - 1] == '.'):
                    tria_count += 1

                if (board[x][y] == '.' and board[x][y] == tile) and (board[x + 1][y - 1] == tile and board[x + 2][y - 2] == '.'):
                    tria_count += 2

                if (board[x][y] == '.' and board[x][y] == tile) and (board[x + 1][y - 1] == tile and board[x + 2][y - 2] == tile) and (board[x + 3][y - 3] == '.'):
                    tria_count += 3

                if (board[x][y] == '.' and board[x][y] == untile) and (board[x + 1][y - 1] == '.'):
                    ntria_count += 1

                if (board[x][y] == '.' and board[x][y] == untile) and (board[x + 1][y - 1] == untile and board[x + 2][y - 2] == '.'):
                    ntria_count += 2

                if (board[x][y] == '.' and board[x][y] == untile) and (board[x + 1][y - 1] == untile and board[x + 2][y - 2] == untile) and (board[x + 3][y - 3] == '.'):
                    ntria_count += 3

        # check diagonal \
        for x in range(self.n - 4):
            for y in range(self.n - 4):
                if (board[x][y] == '.' and board[x + 1][y + 1] == tile) and (board[x + 2][y + 2] == '.'):
                    tria_count += 1

                if (board[x][y] == '.' and board[x + 1][y + 1] == tile) and (board[x + 2][y + 2] == tile and board[x + 3][y + 3] == '.'):
                    tria_count += 2

                if (board[x][y] == '.' and board[x + 1][y + 1] == tile) and (board[x + 2][y + 2] == tile and board[x + 3][y + 3] == tile) and (board[x + 4][y + 4] == '.'):
                    tria_count += 3

                if (board[x][y] == '.' and board[x + 1][y + 1] == untile) and (board[x + 2][y + 2] == '.'):
                    ntria_count += 1

                if (board[x][y] == '.' and board[x + 1][y + 1] == untile) and (board[x + 2][y + 2] == untile and board[x + 3][y + 3] == '.'):
                    ntria_count += 2

                if (board[x][y] == '.' and board[x + 1][y + 1] == untile) and (board[x + 2][y + 2] == untile and board[x + 3][y + 3] == untile) and (board[x + 4][y + 4] == '.'):
                    ntria_count += 3

        return tria_count - ntria_count

    def heuristic1(self, board):
        ##looks at the isWinner function to find # of possible MAX wins - # of possible MIN wins
        win_count = 0
        lose_count = 0

        tile = '0'
        untile = '1'

        rango4 = range(self.n - 4)

        rango = range(self.n)

        # check horizontal spaces
        for y in rango:
            for x in rango4:
                if (board[x][y] == tile or board[x][y] == '.') and (board[x + 1][y] == tile or board[x + 1][y] == '.') and (board[x + 2][y] == tile or board[x + 2][y] == '.') and (board[x + 3][y] == tile or board[x + 3][y] == '.') and (board[x + 4][y] == tile or board[x + 4][y] == '.'):
                    win_count += 1

                if (board[x][y] == untile or board[x][y] == '.') and (board[x + 1][y] == untile or board[x + 1][y] == '.') and (board[x + 2][y] == untile or board[x + 2][y] == '.') and (board[x + 3][y] == untile or board[x + 3][y] == '.') and (board[x + 4][y] == untile or board[x + 4][y] == '.'):
                    lose_count += 2

        # check vertical spaces
        for x in rango:
            for y in rango4:
                if (board[x][y] == tile or board[x][y] == '.') and (board[x][y + 1] == tile or board[x][y + 1] == '.') and (board[x][y + 2] == tile or board[x][y + 2] == '.') and (board[x][y + 3] == tile or board[x][y + 3] == '.') and (board[x][y + 4] == tile or board[x][y + 4] == '.'):
                    win_count += 1

                if (board[x][y] == untile or board[x][y] == '.') and (board[x][y + 1] == untile or board[x][y + 1] == '.') and (board[x][y + 2] == untile or board[x][y + 2] == '.') and (board[x][y + 3] == untile or board[x][y + 3] == '.') and (board[x][y + 4] == untile or board[x][y + 4] == '.'):
                    lose_count += 2

        # check / diagonal spaces
        for x in rango4:
            for y in range(4, self.n):
                if (board[x][y] == tile or board[x][y] == '.') and (board[x + 1][y - 1] == tile or board[x + 1][y - 1] == '.') and (board[x + 2][y - 2] == tile or board[x + 2][y - 2] == '.') and (board[x + 3][y - 3] == tile or board[x + 3][y - 3] == '.') and (board[x + 4][y - 4] == tile or board[x + 4][y - 4] == '.'):
                    win_count += 1

                if (board[x][y] == untile or board[x][y] == '.') and (board[x + 1][y - 1] == untile or board[x + 1][y - 1] == '.') and (board[x + 2][y - 2] == untile or board[x + 2][y - 2] == '.') and (board[x + 3][y - 3] == untile or board[x + 3][y - 3] == '.') and (board[x + 4][y - 4] == untile or board[x + 4][y - 4] == '.'):
                    lose_count += 2

        # check \ diagonal spaces
        for x in rango4:
            for y in rango4:
                if (board[x][y] == tile or board[x][y] == '.') and (board[x + 1][y + 1] == tile or board[x + 1][y + 1] == '.') and (board[x + 2][y + 2] == tile or board[x + 2][y + 2] == '.') and (board[x + 3][y + 3] == tile or board[x + 3][y + 3] == '.') and (board[x + 4][y + 4] == tile or board[x + 3][y + 4] == '.'):
                    win_count += 1

                if (board[x][y] == untile or board[x][y] == '.') and (board[x + 1][y + 1] == untile or board[x + 1][y + 1] == '.') and (board[x + 2][y + 2] == untile or board[x + 2][y + 2] == '.') and (board[x + 3][y + 3] == untile or board[x + 3][y + 3] == '.') and (board[x + 4][y + 4] == untile or board[x + 4][y + 4] == '.'):
                    lose_count += 2

        return win_count - lose_count


    def isValidMove(self, board, move):
        if move[0] >= 0 and move[0] < self.n and move[1] >= 0 and move[1] < self.n:
            return board[move[0]][move[1]] == '.'
        return False

    def isCaptureMove(self, board, jugador, move):
        ##check to see if the move made is going to capture
        ccount = 0
        if jugador == '0':
            contrincante = '1'
        else:
            contrincante = '0'

        ##check horizontal captures
        if (move[1] > 2 and board[move[0]][move[1] - 1] == contrincante and board[move[0]][move[1] - 2] == contrincante and board[move[0]][move[1] - 3] == jugador):
            board[move[0]][move[1] - 1] = '.'
            board[move[0]][move[1] - 2] = '.'
            ccount += 1

        if (move[1] < self.n - 3 and board[move[0]][move[1] + 1] == contrincante and board[move[0]][move[1] + 2] == contrincante and board[move[0]][move[1] + 3] == jugador):
            board[move[0]][move[1] + 1] = '.'
            board[move[0]][move[1] + 2] = '.'
            ccount += 1

        ##check vertical captures
        if (move[0] > 2 and board[move[0] - 1][move[1]] == contrincante and board[move[0] - 2][move[1]] == contrincante and board[move[0] - 3][move[1]] == jugador):
            board[move[0] - 1][move[1]] = '.'
            board[move[0] - 2][move[1]] = '.'
            ccount += 1

        if (move[0] < self.n - 3 and board[move[0] + 1][move[1]] == contrincante and board[move[0] + 2][move[1]] == contrincante and board[move[0] + 3][move[1]] == jugador):
            board[move[0] + 1][move[1]] = '.'
            board[move[0] + 2][move[1]] = '.'
            ccount += 1

        ##check diagonal cpatures
        if (move[0] > 2 and move[1] > 2 and board[move[0] - 1][move[1] - 1] == contrincante and board[move[0] - 2][move[1] - 2] == contrincante and board[move[0] - 3][move[1] - 3] == jugador):
            board[move[0] - 1][move[1] - 1] = '.'
            board[move[0] - 2][move[1] - 2] = '.'
            ccount += 1

        if (move[0] < self.n - 3 and move[1] < self.n - 3 and board[move[0] + 1][move[1] + 1] == contrincante and board[move[0] + 2][move[1] + 2] == contrincante and board[move[0] + 3][move[1] + 3] == jugador):
            board[move[0] + 1][move[1] + 1] = '.'
            board[move[0] + 2][move[1] + 2] = '.'
            ccount += 1

        ##check other diagonal captures
        if (move[0] > 2 and move[1] < self.n - 3 and board[move[0] - 1][move[1] + 1] == contrincante and board[move[0] - 2][move[1] + 2] == contrincante and board[move[0] - 3][move[1] + 3] == jugador):
            board[move[0] - 1][move[1] + 1] = '.'
            board[move[0] - 2][move[1] + 2] = '.'
            ccount += 1

        if (move[0] < self.n - 3 and move[1] < self.n - 3 and board[move[0] + 1][move[1] - 1] == contrincante and board[move[0] + 2][move[1] - 2] == contrincante and board[move[0] + 3][move[1] - 3] == jugador):
            board[move[0] + 1][move[1] - 1] = '.'
            board[move[0] + 2][move[1] - 2] = '.'
            ccount += 1

        return ccount

    def isCaptureMoveSimple(self, board, jugador, move):
        if jugador == '0':
            contrincante = '1'
        else:
            contrincante = '0'

        ##check horizontal captures
        if (move[1] > 2 and board[move[0]][move[1] - 1] == contrincante and board[move[0]][move[1] - 2] == contrincante and board[move[0]][move[1] - 3] == jugador):
            board[move[0]][move[1] - 1] = '.'
            board[move[0]][move[1] - 2] = '.'

        if (move[1] < self.n - 3 and board[move[0]][move[1] + 1] == contrincante and board[move[0]][move[1] + 2] == contrincante and board[move[0]][move[1] + 3] == jugador):
            board[move[0]][move[1] + 1] = '.'
            board[move[0]][move[1] + 2] = '.'

        ##check vertical captures
        if (move[0] > 2 and board[move[0] - 1][move[1]] == contrincante and board[move[0] - 2][move[1]] == contrincante and board[move[0] - 3][move[1]] == jugador):
            board[move[0] - 1][move[1]] = '.'
            board[move[0] - 2][move[1]] = '.'

        if (move[0] < self.n - 3 and board[move[0] + 1][move[1]] == contrincante and board[move[0] + 2][move[1]] == contrincante and board[move[0] + 3][move[1]] == jugador):
            board[move[0] + 1][move[1]] = '.'
            board[move[0] + 2][move[1]] = '.'

        ##check diagonal cpatures
        if (move[0] > 2 and move[1] > 2 and board[move[0] - 1][move[1] - 1] == contrincante and board[move[0] - 2][move[1] - 2] == contrincante and board[move[0] - 3][move[1] - 3] == jugador):
            board[move[0] - 1][move[1] - 1] = '.'
            board[move[0] - 2][move[1] - 2] = '.'


        if (move[0] < self.n - 3 and move[1] < self.n - 3 and board[move[0] + 1][move[1] + 1] == contrincante and board[move[0] + 2][move[1] + 2] == contrincante and board[move[0] + 3][move[1] + 3] == jugador):
            board[move[0] + 1][move[1] + 1] = '.'
            board[move[0] + 2][move[1] + 2] = '.'

        ##check other diagonal captures
        if (move[0] > 2 and move[1] < self.n - 3 and board[move[0] - 1][move[1] + 1] == contrincante and board[move[0] - 2][move[1] + 2] == contrincante and board[move[0] - 3][move[1] + 3] == jugador):
            board[move[0] - 1][move[1] + 1] = '.'
            board[move[0] - 2][move[1] + 2] = '.'

        if (move[0] < self.n - 3 and move[1] < self.n - 3 and board[move[0] + 1][move[1] - 1] == contrincante and board[move[0] + 2][move[1] - 2] == contrincante and board[move[0] + 3][move[1] - 3] == jugador):
            board[move[0] + 1][move[1] - 1] = '.'
            board[move[0] + 2][move[1] - 2] = '.'

    ##change board state, move is tuple(x, y)
    def makeMove(self, board, player, move):
        self.isCaptureMoveSimple(board, player, move)
        board[move[0]][move[1]] = player

    def makeCMove(self, board, player, move):
        captures = self.isCaptureMove(board, player, move)
        board[move[0]][move[1]] = player
        if captures != 0:
            if player == '0':
                self.wcaptures += captures
            else:
                self.bcaptures += captures
        print(self.bcaptures, self.wcaptures)

    def getPrevMove(self):
        return self.prevMove

    def isBoardFull(self, board):
        for row in range(self.n):
            for col in range(self.n):
                if board[row][col] == '.':
                    return False
        return True

    def isWinner(self, board, tile):
        ##checking horizontal spaces

        rango = range(self.n)
        rango4 = range(self.n - 4)

        for y in rango:
            for x in rango4:
                if board[x][y] == tile and board[x + 1][y] == tile and board[x + 2][y] == tile and board[x + 3][y] == tile and board[x + 4][y] == tile:
                    return True

        ##checking for vertical spaces
        for x in rango:
            for y in rango4:
                if board[x][y] == tile and board[x][y + 1] == tile and board[x][y + 2] == tile and board[x][y + 3] == tile and board[x][y + 4] == tile:
                    return True

        ##checking for diagonal spaces
        for x in rango4:
            for y in range(4, self.n):
                if board[x][y] == tile and board[x + 1][y - 1] == tile and board[x + 2][y - 2] == tile and board[x + 3][y - 3] == tile and board[x + 4][y - 4] == tile:
                    return True

        ##check other diagonal spaces
        for x in rango4:
            for y in rango4:
                if board[x][y] == tile and board[x + 1][y + 1] == tile and board[x + 2][y + 2] == tile and board[x + 3][y + 3] == tile and board[x + 4][y + 4] == tile:
                    return True

        ##checking capture pairs
        if tile == '1':
            if self.wcaptures >= 5:
                return True
        else:
            if self.bcaptures >= 5:
                return True
        return False

