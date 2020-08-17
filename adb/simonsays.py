#!./env/bin/python

from ppadb.client import Client
import mss
import mss.tools

GREEN = (44, 184, 50)
RED = (184, 45, 44)
YELLOW = (181, 183, 41)
BLUE = (45, 80, 184)
COLORS = [GREEN, RED, YELLOW, BLUE]

adb = Client(host="127.0.0.1", port=5037)
device = adb.devices()[0]

sct = mss.mss
screen = {"top": 320, "left": 107, "width": 127, "height": 127}
sequence = []

def play(sequence):
    for p in sequence:
        device.shell(f"input tap {p[0]} {p[1]}")
    return([])


device.shell(f"input tap 540 1080")
while True:
    shot = sct().grab(screen)
    positions = [(300, 600), (800, 600), (300, 1600), (600, 1600)]
    greenp = shot.pixel(0, 0)
    redp = shot.pixel(126, 0)
    yellowp = shot.pixel(0, 126)
    bluep = shot.pixel(126, 126)
    pixels = [greenp, redp, yellowp, bluep]
    s = 0
    for i, p in enumerate(pixels):
        if p != COLORS[i] and not positions[i] in sequence:
            print(p)
            sequence.append(positions[i])
        elif p == COLORS[i]:
            s += 1
    if s == 4:
        sequence = play(sequence)
