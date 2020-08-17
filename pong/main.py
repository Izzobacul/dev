#!./env/bin/python

import pygame
import time

WIDTH = 600
HEIGHT = 600

class Bar:
    def __init__(self, width, height, side):
        self.y = (HEIGHT//2) - height//2
        self.width = width
        self.height = height
        self.yspeed = 0
        self.side = side
        if side == 1:
            self.x = WIDTH-(self.width*2)
        elif side == 0:
            self.x = self.width

    def show(self, screen):
        if self.side == 1:
            pygame.draw.rect(screen, (255, 255, 255), (int(self.x), int(self.y), self.width, self.height))
        elif self.side == 0:
            pygame.draw.rect(screen, (255, 255, 255), (int(self.x), int(self.y), self.width, self.height))

    def move(self):
        self.y += self.yspeed
        if self.y > HEIGHT - self.height:
            self.y = HEIGHT - self.height
        elif self.y < 0:
            self.y = 0

class Ball:
    def __init__(self, r):
        self.x = int(WIDTH/2)
        self.y = int(HEIGHT/2)
        self.r = r
        self.yspeed = -0.5
        self.xspeed = 9.5

    def show(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.r, 0)

    def move(self, p1, p2):
        self.x += self.xspeed
        self.y += self.yspeed
        s = 10
        if self.y + self.r > HEIGHT or self.y - self.r < 0:
            self.yspeed *= -1

        if self.x > p1.x - self.r and (self.y > p1.y and self.y < p1.y + p1.height):
            self.xspeed *= -1
            d = self.y - (p1.y + p1.height/2)
            n = d / ((p1.height/2) * 1.5)
            self.yspeed = s * n

        if self.x < p2.x + p2.width + self.r and (self.y > p2.y and self.y < p2.y + p2.height):
            self.xspeed *= -1
            d = self.y - (p2.y + p2.height/2)
            n = d / ((p2.height/2) * 1.5)
            self.yspeed = s * n

def show(objs, screen):
    screen.fill(0)
    for o in objs:
        o.show(screen)
    pygame.display.update()

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    p1 = Bar(20, 200, 1)
    p2 = Bar(20, 200, 0)
    b = Ball(10)
    objs = [p1, p2, b]

    running = True
    while running:
        p1.move()
        p2.move()

        if b.x > WIDTH:
            print("P2 scored!")
            b.__init__(10)
            show(objs, screen)
            time.sleep(1)
        elif b.x < 0:
            print("P1 scored!")
            b.__init__(10)
            show(objs, screen)
            time.sleep(1)
        b.move(p1, p2)

        show(objs, screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    p1.yspeed = -2.5
                elif event.key == pygame.K_DOWN:
                    p1.yspeed = 2.5
                if event.key == pygame.K_w:
                    p2.yspeed = -2.5
                elif event.key == pygame.K_s:
                    p2.yspeed = 2.5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    p1.yspeed = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    p2.yspeed = 0

    pygame.quit()

if __name__ == '__main__':
    main()
