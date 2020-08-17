#!/usr/bin/env python3

import random

class Dice:
    def __init__(self, sides):
        self.result = random.randint(1, sides)

    def __str__(self) -> str:
        return str(self.result)

if __name__ == '__main__':
    print("Enter the dice you want to roll separated by a space:")
    sides = list(map(int, input().split(" ")))
    dice = [Dice(s) for s in sides]
    for i, d in enumerate(dice):
        print(f"The result for the dice {sides[i]} is {d}")
