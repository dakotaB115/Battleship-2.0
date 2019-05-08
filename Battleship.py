import random
import sys
import os

grid_ai = [["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [
    "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]]

grid_player = [["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [
    "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]]

grid_top = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# Display the grid


def display_player():
    y = 0
    print(grid_top)
    while y < 10:
        print(grid_player[y])
        y += 1


def display_ai():
    y = 0
    print(grid_top)
    while y < 10:
        print(grid_ai[y])
        y += 1


def y_detector(y):
    if y < 0:
        print("negative")
    elif y > 9:
        print("positive")


def up(x, y, piece):
    while piece > 0:
        piece -= 1
        y += 1
        grid_ai[y][x] = "x"


def down(x, y, piece):
    while piece > 0:
        piece -= 1
        y -= 1
        grid_ai[y][x] = "x"


def left(x, y, piece):
    while piece > 0:
        piece -= 1
        x -= 1
        grid_ai[y][x] = "x"


def right(x, y, piece):
    while piece > 0:
        piece -= 1
        x += 1
        grid_ai[y][x] = "x"


# def AI_grid_init():
#     r = 0
#     p = 0
#     z = 8
#     for i in range(5):
#         o = random.randint(1, 5)
#         r += 1

#         if r == 1:
#             p = 2
#         elif r == 2 or r == 3:
#             p = 3
#         elif r == 4:
#             p = 4
#         elif r == 5:
#             p = 5

#         if o == 1:
#             x = random.randint(0, z)
#             print("Up x:" + str(x))
#             y = random.randint(0, z)
#             print("Up y:" + str(y))
#             up(x, y, p)
#         elif o == 2:
#             x = random.randint(0, z)
#             print("Down x:" + str(x))
#             y = random.randint(0, z)
#             print("Down y:" + str(y))
#             down(x, y, p)
#         elif o == 3:
#             x = random.randint(0, z)
#             print("Left x:" + str(x))
#             y = random.randint(0, z)
#             print("Left y:" + str(y))
#             left(x, y, p)
#         elif o == 4:
#             x = random.randint(0, z)
#             print("Right x:" + str(x))
#             y = random.randint(0, z)
#             print("Right y:" + str(y))
#             right(x, y, p)

def AI_grid_init():
    r = 0
    p = 0
    for i in range(5):
        o = 1
        r += 1
        if r == 1 or r == 2:
            p = r + 1
        else:
            p = r

        if o == 1:
            #     x = random.randint(0, 9)
            #     y = random.randint(0, 9)
            up(1, 8, p)


# Player input


def fire():
    display_player()
    x = int(input("x: ")) - 1
    y = int(input("y: ")) - 1
    grid_player[y][x] = "x"
    if grid_ai[y][x] == "x":
        os.system("clear")
        print("HIT")
    else:
        os.system("clear")
        print("MISS")


AI_grid_init()
display_ai()
# turns = 20
# while turns > 0:
#     display_ai()
#     turns -= 1
#     print("Turns left: " + str(turns))
#     fire()
#     if turns == 0:
#         os.system("clear")
#         print("Goodbye")
#         sys.exit()
