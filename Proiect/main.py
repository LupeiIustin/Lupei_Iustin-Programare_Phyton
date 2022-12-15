import copy
import sys
import pygame
import random
import numpy as np

from const import *


# --- PYGAME SETUP ---

pygame.init()
screen = pygame.display.set_mode((600, 600))    # dimensiunea ferestrei de joc (latime si inaltime)
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

        # asignam coloanei si liniei playerul dupa apasare
    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

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
