#!./env/bin/python

import pygame

class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class King(Piece):
    def __init__(self)

def main():
    pygame.init()

    screen = pygame.display.set_mode((700, 700))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == '__main__':
    main()
