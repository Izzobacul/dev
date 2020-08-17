#!./env/bin/python

import pygame
import random

class Board:
    def __init__(self):
        self.grid = [[None for j in range(4)] for i in range(4)]
        self.set_start()
        self.set_start()
        print(self.grid)

    def set_start(self):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while self.grid[y][x] != None:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        self.grid[y][x] = random.choice([2, 2, 2, 2, 2, 4])

    def show(self):
        

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("2048")

    board = Board()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == '__main__':
    main()
