#!/usr/bin/env python
import pygame, sys
from pygame import Rect
import random

pygame.init()

pygame.display.set_caption("Gato")
icon = pygame.image.load("/Users/izzobacul/dev/auto_gato/icon.png")
pygame.display.set_icon(icon)

gamemode = 1
size = width, height = 400, 400
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
stroke = 4
turn = 1
winn = False
font = pygame.font.Font("freesansbold.ttf", 50)
round = 0

screen = pygame.display.set_mode(size)

def draw_X(rect, screen, color, stroke):
    pygame.draw.line(screen, color, (rect.left, rect.top), (rect.left+rect.width, rect.top + rect.height), stroke)
    pygame.draw.line(screen, color, (rect.left+rect.width, rect.top), (rect.left, rect.top + rect.height), stroke)

def win(winner):
    global winn
    if winner==1:
        print("X WINS!!")
    else:
        print("O WINS!!")
    text = font.render(f"{('', 'X', 'O')[winner]} WINS!!", True, red, black)
    screen.blit(text, (int(width/2-text.get_width()/2), int(height/2-text.get_height()/2)))
    winn = True
    pygame.display.update()
    pygame.time.wait(1000)

def tie():
    text = font.render("IT'S A TIE", True, red, black)
    screen.blit(text, (int(width/2-text.get_width()/2), int(height/2-text.get_height()/2)))
    global winn
    winn = True

def restart(res):
    global round
    text = font.render("Restart?", True, red, black)
    screen.blit(text, (int(width/2-text.get_width()/2), int(height/2-text.get_height()/2+height/4)))
    pygame.display.update()
    if res:
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0]>int(width/2-text.get_width()/2) and mouse_pos[0]<int(width/2+text.get_width()/2) and mouse_pos[1]>int(height/2-text.get_height()/2+height/4) and mouse_pos[1]<int(height/2+text.get_height()/2+height/4):
            global winn
            winn = False
            screen.fill(black)
            global board
            del board
            board = Board(screen, size, stroke)
            global turn
            turn = 1
            print("RESTARTED")
            board.show()

def computer_play(slots):
    global turn
    global board
    slotsc = slots.copy()

    #Line winning
    for i in range(0, 3):
        if slotsc[i][0] == slotsc[i][2] == 2 or slotsc[i][0] == slotsc[i][1] == 2 or slotsc[i][1] == slotsc[i][2] == 2:
            for l in range(0, 3):
                if slotsc[i][l] == 0:
                    board.slots[i][l] = 2
                    turn = 1
                    return
        if slotsc[0][i] == slotsc[2][i] == 2 or slotsc[0][i] == slotsc[1][i] == 2 or slotsc[1][i] == slotsc[2][i] == 2:
            for l in range(0, 3):
                if slotsc[l][i] == 0:
                    board.slots[l][i] = 2
                    turn = 1
                    return
    #
    #Diagonal winning
    if slotsc[0][0] == slotsc[1][1] == 2 or slotsc[0][0] == slotsc[2][2] == 2 or slotsc[2][2] == slotsc[1][1] == 2:
        for l in range(0, 3):
            if slotsc[l][l] == 0:
                board.slots[l][l] = 2
                turn = 1
                return
    if slotsc[0][2] == slotsc[1][1] == 2 or slotsc[0][2] == slotsc[2][0] == 2 or slotsc[2][0] == slotsc[1][1] == 2:
        if slotsc[0][2] == 0:
            board.slots[0][2] = 2
            turn = 1
            return
        if slotsc[1][1] == 0:
            board.slots[1][1] = 2
            turn = 1
            return
        if slotsc[2][0] == 0:
            board.slots[2][0] = 2
            turn = 1
            return
    #
    #Line blocking
    for i in range(0, 3):
        if slotsc[i][0] == slotsc[i][2] == 1 or slotsc[i][0] == slotsc[i][1] == 1 or slotsc[i][1] == slotsc[i][2] == 1:
            for l in range(0, 3):
                if slotsc[i][l] == 0:
                    board.slots[i][l] = 2
                    turn = 1
                    return
        if slotsc[0][i] == slotsc[2][i] == 1 or slotsc[0][i] == slotsc[1][i] == 1 or slotsc[1][i] == slotsc[2][i] == 1:
            for l in range(0, 3):
                if slotsc[l][i] == 0:
                    board.slots[l][i] = 2
                    turn = 1
                    return
    #
    #Diagonal blocking
    if slotsc[0][0] == slotsc[1][1] == 1 or slotsc[0][0] == slotsc[2][2] == 1 or slotsc[2][2] == slotsc[1][1] == 1:
        for l in range(0, 3):
            if slotsc[l][l] == 0:
                board.slots[l][l] = 2
                turn = 1
                return
    if slotsc[0][2] == slotsc[1][1] == 1 or slotsc[0][2] == slotsc[2][0] == 1 or slotsc[2][0] == slotsc[1][1] == 1:
        if slotsc[0][2] == 0:
            board.slots[0][2] = 2
            turn = 1
            return
        if slotsc[1][1] == 0:
            board.slots[1][1] = 2
            turn = 1
            return
        if slotsc[2][0] == 0:
            board.slots[2][0] = 2
            turn = 1
            return
    #
    #Opposing corner blocking
    if (slotsc[0].count(2) + slotsc[1].count(2) + slotsc[2].count(2)) > 0:
        if slotsc[0][0] == 1 and slotsc[2][2] == 0:
            board.slots[2][2] = 2
            turn = 1
            return
        if slotsc[2][2] == 1 and slotsc[0][0] == 0:
            board.slots[0][0] = 2
            turn = 1
            return
        if slotsc[0][2] == 1 and slotsc[2][0] == 0:
            board.slots[2][0] = 2
            turn = 1
            return
        if slotsc[2][0] == 1 and slotsc[0][2] == 0:
            board.slots[0][2] = 2
            turn = 1
            return
    #
    #Middle if empty
    if slotsc[1][1] == 0:
        board.slots[1][1] = 2
        turn = 1
        return
    #
    #Random corner
    empty = []
    for n in ((1, 1), (0, 0), (2, 0), (0, 2), (2, 2)):
        if slotsc[n[0]][n[1]] == 0:
            empty.append(n)
    rand = random.randrange(0, len(empty))
    if len(empty)>0:
        board.slots[empty[rand][0]][empty[rand][1]] = 2
        turn = 1
        return
    #
    #Random any
    empty = []
    for x in range(0, 3):
        for y in range(0, 3):
            if slotsc[x][y] == 0:
                empty.append((x, y))
    rand = random.randrange(0, len(empty))
    board.slots[empty[rand][0]][empty[rand][1]] = 2
    turn = 1
    return
    #

class Board:
    def __init__(self, screen, size, stroke):
        self.screen = screen
        self.size = size
        self.stroke = stroke
        #1 = X / 2 = O
        self.slots = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.show()
        pygame.display.update()
    def show(self):
        pygame.draw.line(self.screen, white, (int(self.size[0]/3), 0), (int(self.size[0]/3), self.size[1]), self.stroke)
        pygame.draw.line(self.screen, white, (int(self.size[0]/3*2), 0), (int(self.size[0]/3*2), self.size[1]), self.stroke)
        pygame.draw.line(self.screen, white, (0, int(self.size[1]/3)), (self.size[0], int(self.size[1]/3)), self.stroke)
        pygame.draw.line(self.screen, white, (0, int(self.size[1]/3*2)), (self.size[0], int(self.size[1]/3*2)), self.stroke)
        for x in range(0, len(self.slots)):
            for y in range(0, len(self.slots[x])):
                if (not self.slots[y][x]==0):
                    if self.slots[y][x] == 1:
                        draw_X(Rect(int(x*self.size[0]/3+self.size[0]/20), int(y*self.size[1]/3+self.size[1]/20), int(self.size[0]/3-self.size[0]/10), int(self.size[1]/3-self.size[1]/10)), self.screen, white, self.stroke)
                    elif self.slots[y][x] == 2:
                        pygame.draw.ellipse(screen, white, Rect(int(x*self.size[0]/3+self.size[0]/20), int(y*self.size[1]/3+self.size[1]/20), int(self.size[0]/3-self.size[0]/10), int(self.size[1]/3-self.size[1]/10)), self.stroke)
        #pygame.display.flip()
    def add(self, pos):
        global turn
        for x in range(0, len(self.slots)):
            for y in range(0, len(self.slots[x])):
                if pos[0]>int(self.size[0]/3*x) and pos[0]<int(self.size[0]/3*(x+1)) and pos[1]>int(self.size[1]/3*y) and pos[1]<int(self.size[1]/3*(y+1)):
                    if self.slots[y][x] == 0:
                        if turn == 1:
                            self.slots[y][x] = 1
                            self.show()
                            pygame.display.update()
                            turn = 0
                            self.check()
                            return
                        if turn == 0 and gamemode == 2:
                            self.slots[y][x] = 2
                            self.show()
                            pygame.display.update()
                            turn = 1
                            self.check()
                            return



    def check(self):
        for x in range(0, 3):
            if (self.slots[x][0] == self.slots[x][1] == self.slots[x][2]) and not self.slots[x][0] == 0:
                win(self.slots[x][0])
            if (self.slots[0][x] == self.slots[1][x] == self.slots[2][x]) and not self.slots[0][x] == 0:
                win(self.slots[0][x])
        if (self.slots[0][0] == self.slots[1][1] == self.slots[2][2]) and not self.slots[0][0] == 0:
            win(self.slots[0][0])
        if (self.slots[0][2] == self.slots[1][1] == self.slots[2][0]) and not self.slots[0][2] == 0:
            win(self.slots[0][2])
        for x in self.slots:
            for y in x:
                if y == 0:
                    return
        tie()


board = Board(screen, size, stroke)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not winn: board.add(pygame.mouse.get_pos())
            if turn == 0 and gamemode == 1 and not winn:
                computer_play(board.slots)
                board.show()
                pygame.display.update()
                board.check()
            if winn:
                restart(True)

    if winn:
        restart(False)
