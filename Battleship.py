import random
import sys
import os

grid_ai = [["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]]

grid_player = [["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]]

# Display the grid
def display_player():
    y = 0
    while y < 10:
        print(grid_player[y])
        y += 1


def display_ai():
    y = 0
    while y < 10:
        print(grid_ai[y])
        y += 1

# Initialize the AI grid
# Need to determine orientation (1=up, 2=down, 3=left, 4=right) random.randint(1,4)
# Carrier, with five holes.
# Battleship, with four holes.
# Cruiser, with three holes.
# Submarine, with three holes.
# Destroyer, with two holes.
# Need to get 17 points to win
# Need to make sure ships are not clipping

def writer_pos(x, y, piece):
        row = grid_ai[y]
        while piece > 0:
                x += 1
                row[x] = "x"
                piece -= 1 


def writer_neg(x, y, piece):
        row = grid_ai[y]
        while piece > 0:
                x -= 1
                row[x] = "x"
                piece -= 1
        print(row)

def up(p):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if p == 1:
                writer_pos(y, x, p)
        elif p == 2:
                writer_pos(y, x, p)
        elif p == 3:
                writer_pos(y, x, p)
        elif p == 4:
                writer_neg(y, x, p)


def down():
        print("down")

def left():
        print("left")

def right():
        print("right")

def AI_grid_init():
        # o = random.randint(1, 4)
        o = 1
        pieces = []
        piece = 0
        for i in range(5):
                        r = random.randint(1, 4)
                        if r not in pieces:
                                pieces.append(r)
                                piece = r
        if o == 1:
                up(piece)
        # elif o == 2:

        # elif o == 3:

        # elif o == 4:

AI_grid_init()
display_ai()

# Player input
def shoot(x, y):
    x -= 1
    y -= 1
    grid_player[y][x] = "x"

def fire():
    display_player()
    x = int(input("x: ")) - 1
    y = int(input("y: ")) - 1
    shoot(x, y)
    if grid_ai[y][x] == "x":
        os.system("cls")
        print("HIT")
    else:
        os.system("cls")
        print("MISS")

# Builder
# turns = 1
# while turns > 0:
#     turns -= 1
#     print("Turns left: " + str(turns))
#     fire()
#     if turns == 0:
#         os.system("cls")
#         print("Goodbye")
#         sys.exit()
