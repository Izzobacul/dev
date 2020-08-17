from mss import mss
import time
from PIL import Image

#OPEN https://es.jstris.jezevec10.com/ on guest

COLORS ={
    (37, 155, 213): 'I',
    (175, 33, 136): 'T',
    (87, 178, 35): 'S',
    (214, 0, 54): 'Z',
    (225, 88, 13): 'L',
    (47, 63, 195): 'J',
    (225, 158, 30): 'O',
    (0, 0, 0): 'NONE'
}

def get_pieces():
    monitor = mss().monitors[0]
    scr = mss().grab(monitor)
    img = Image.frombytes("RGB", scr.size, scr.rgb, "raw")

    hold_pixs = [img.getpixel((194, 196)), img.getpixel((169, 267)), img.getpixel((190, 272))]
    hold = "NONE"
    for p in hold_pixs:
        if p in COLORS.keys():
            hold = COLORS[p]

    incoming = img.getpixel((370, 215))
    if incoming in COLORS.keys():
        incoming = COLORS[incoming]
    else:
        incoming = "NONE"

    grid = [[]]*20
    y = 0
    for i in range(204+12, 684, 24):
        grid[y] = []
        for l in range(264+12, 504, 24):
            pix = ()
            pix = img.getpixel((l, i))
            if pix==(0, 0, 0):
                grid[y].append(0)
            else:
                grid[y].append(1)
        y+=1
    return(grid, hold, incoming)

def evaluate_posible_moves(grid, incoming, hold):
    return 0

def main():
    grid, hold, incoming = get_pieces()
    move = evaluate_posible_moves(grid, incoming, hold)

def test():
    scr = mss().grab(mss().monitors[1])
    img = Image.frombytes("RGB", scr.size, scr.rgb, "raw")
    print(img.getpixel((600, 400)))


if __name__=='__main__':
    while True:
        main()