#!/usr/bin/env python3

import os
import random
import time
import sys

help = '''
Welcome to Rock Paper Scissors.
There are 2 game-modes available: Normal and Extended

Normal rules:
1.- Choose your move: Rock, Paper or Scissors
2.- The computer will choose a random move
3.- Rock destroys Scissors, Paper covers Rock and Scissors cut Paper

Extended rules:
1.- Choose your move: Rock, Gun, Lightning, Devil, Dragon, Water, Air, Paper,
    Sponge, Wolf, Tree, Human, Snake, Scissors, Fire
2.- The computer will choose a random move
3.- The following is what wins against what:
    Rock: Scissors, Snake, Human, Tree, Wolf, Sponge, Fire
    Gun: Fire, Scissors, Snake, Human, Tree, Wolf, Rock
    Lightning: Rock, Fire, Scissors, Snake, Human, Tree, Gun
    Devil: Gun, Rock, Fire, Scissors, Snake, Human, Lightning
    Dragon: Lightning, Gun, Rock, Fire, Scissors, Snake, Devil
    Water: Devil, Lightning, Gun, Rock, Fire, Scissors, Dragon
    Air: Dragon, Devil, Lightning, Gun, Rock, Fire, Water
    Paper: Water, Dragon, Devil, Lightning, Gun, Rock, Air
    Sponge: Air, Water, Dragon, Devil, Lightning, Gun, Paper
    Wolf: Paper, Air, Water, Dragon, Devil, Lightning, Sponge
    Tree: Sponge, Paper, Air, Water, Dragon, Devil, Wolf
    Human: Wolf, Sponge, Paper, Air, Water, Dragon, Tree
    Snake: Tree, Wolf, Sponge, Paper, Air, Water, Human
    Scissors: Human, Tree, Wolf, Sponge, Paper, Air, Snake
    Fire: Snake, Human, Tree, Wolf, Sponge, Paper, Scissors
'''

normal = {
    'rock': ['scissors'],
    'scissors': ['paper'],
    'paper': ['rock']
}

extended = {
    'rock': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'fire'],
    'gun': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'rock'],
    'lightning': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'gun'],
    'devil': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'lightning'],
    'dragon': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'devil'],
    'water': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'dragon'],
    'air': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'water'],
    'paper': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'air'],
    'sponge': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'paper'],
    'wolf': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'sponge'],
    'tree': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'wolf'],
    'human': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'tree'],
    'snake': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'human'],
    'scissors': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'snake'],
    'fire': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'scissors']
}

def main():
    mode = [normal, extended][int(input("Do you want to play: \n0: Normal\n1: Extended\n"))]
    playing = True
    while playing:
        os.system('clear')
        moves = mode
        move = random.choice(list(moves.keys()))
        print("Choose your move: ")
        for i, m in enumerate(moves.keys()):
            print(f"{i}: {m.capitalize()}")
        while True:
            try:
                player_move = list(moves.keys())[int(input())]
                break
            except IndexError:
                print("Please choose a move in the list")
        print(f"You chose {player_move.capitalize()}")
        print(f"The computer chose {move.capitalize()}")
        time.sleep(0.5)
        if move in moves[player_move]:
            print("You win!")
        elif move == player_move:
            print("It's a tie!")
        else:
            print("You lose :(")
        time.sleep(0.5)
        again = input("Do you want to play again? (y/n) ")
        if not 'y' in again:
            playing = False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print(help)
            exit()
    main()
