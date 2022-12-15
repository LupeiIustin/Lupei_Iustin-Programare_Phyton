import copy
import sys
import pygame
import random
import numpy as np

from const import *


# --- PYGAME SETUP ---

pygame.init()
screen = pygame.display.set_mode((1000, 600))    # dimensiunea ferestrei de joc (latime si inaltime)
pygame.display.set_caption('TIC TAC TOE AI')
myfont = pygame.font.SysFont("Times New Roman", 30)
black = (0, 0, 0)
screen.fill(BG_COLOR)


# --- CLASSES ---

class Board:
    # initializam tabla de joc
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))    #salvam progresul jocului intr o matricesi asignam 0 ca start
        self.empty_sqrs = self.squares  # [squares]1
        self.marked_sqrs = 0 #in #
        # vericam daca avem 3 de x/0 pe verticala/orizontala/diagonale

    # verificam daca a castigat unul din playeri
    def final_state(self, show=False):
        '''
            @return 0 if there is no win yet
            @return 1 if player 1 wins
            @return 2 if player 2 wins
        '''

        # vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0: #daca gasim 3 piese de acelasi fel
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20) # formula pentru aflarea pct de start al liniei
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20) # final
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH) #desenam o linie pt a marca win
                return self.squares[0][col]

        # horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    iPos = (20, row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]

        # desc diagonal
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, 20)
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # asc diagonal
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, HEIGHT - 20)
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # no win yet
        return 0

        # asignam coloanei si liniei playerul dupa apasare

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_sqr(self, row, col):
        if row < 3 and col < 3:
            return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row, col))

        return empty_sqrs

    def isfull(self):
        return self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0
class Game:

    def __init__(self):
        self.board = Board()
        self.player = 1  # 1-cross  #2-circles
        self.running = True
        self.show_lines()

    # --- DRAW METHODS ---

        # desenam liniile orizontale si verticale pentru joc vizual
    def show_lines(self):
        # bg
        screen.fill(BG_COLOR)

        # vertical
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)



def main():
    # --- OBJECTS ---

    game = Game()
    board = game.board

    # --- MAINLOOP ---

    while True:
        # pygame events
        for event in pygame.event.get():
            # click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                #  mark sqr
                if board.empty_sqr(row, col) and game.running:
                    game.make_move(row, col)

                    if game.isover():
                        game.running = False
        pygame.display.update()

main()
