#!./env/bin/python

from ppadb.client import Client
import mss
import mss.tools

BLACK = (29, 29, 29)

adb = Client(host="127.0.0.1", port=5037)
device = adb.devices()[0]

sct = mss.mss
screen = {"top": 430, "left": 35, "width": 280, "height": 1}
tile_pos = [(110, 1225), (430, 1225), (746, 1225), (940, 1225)]

while True:
    shot = sct().grab(screen)
    tiles = [shot.pixel(0, 0), shot.pixel(100, 0), shot.pixel(200, 0), shot.pixel(279, 0)]
    for i, t in enumerate(tiles):
        if t == BLACK:
            print(t)
            device.shell(f"input tap {tile_pos[i][0]} {tile_pos[i][1]}")
