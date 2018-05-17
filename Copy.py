# -*- coding: UTF-8 -*-
def deepCopy(board):
    board2 = []

    for x in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
        l = []
        for y in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
            l.append(board[x][y])
        board2.append(l)

    return board2