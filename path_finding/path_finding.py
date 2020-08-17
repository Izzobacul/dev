import pygame

pygame.init()

WIDTH = 700
HEIGHT = 700
SCREEN = pygame.display.set_mode(size=(WIDTH, HEIGHT))
SCREEN.fill((255, 255, 255))

class Grid():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.sqw = int(WIDTH/self.w)
        self.sqh = int(HEIGHT/self.h)
        self.grid = [[[0, 0, 0, (0, 0, 0), 2, True]for l in range(w)]for i in range(h)]
        self.start = [-1, -1]
        self.end = [-1, -1]
    def show(self):
        SCREEN.fill((255, 255, 255))
        for y, r in enumerate(self.grid):
            for x, c in enumerate(r):
                left = int(x*(WIDTH/self.w))
                top = int(y*(HEIGHT/self.h))
                width = self.sqw
                height = self.sqh
                pygame.draw.rect(SCREEN, c[3], (left, top, width, height), width=c[4])
        pygame.display.flip()
    def set_start(self, pos):
        x, y = pos[0]//self.sqw, pos[1]//self.sqh
        if self.start == [x, y]:
            self.start = [-1, -1]
            c = self.grid[y][x]
            c[3] = (0, 0, 0)
            c[4] = 2
            return
        if self.start != [-1, -1]:
            return
        c = self.grid[y][x]
        c[3] = (255, 0, 255)
        c[4] = 0
        self.start = [x, y]
    def set_end(self, pos):
        x, y = pos[0]//self.sqw, pos[1]//self.sqh
        if self.end == [x, y]:
            self.end = [-1, -1]
            c = self.grid[y][x]
            c[3] = (0, 0, 0)
            c[4] = 2
            return
        if self.end != [-1, -1]:
            return
        c = self.grid[y][x]
        c[3] = (0, 255, 255)
        c[4] = 0
        self.end = [x, y]
    def place_walls(self, pos):
        x, y = pos[0]//self.sqw, pos[1]//self.sqh
        if not self.grid[y][x][5]:
            c = self.grid[y][x]
            c[3] = (0, 0, 0)
            c[4] = 2
            c[5] = True
            return
        c = self.grid[y][x]
        c[4] = 0
        c[5] = False
def find_path(grid):
    pass

g = Grid(35, 35)

running = True
while running:
    g.show()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                g.set_start(event.pos)
            elif event.button == 2:
                g.place_walls(event.pos)
            elif event.button == 3:
                g.set_end(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                find_path(g)