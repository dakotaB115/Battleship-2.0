import random
import sys
import os

grid_ai = [["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [
    "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]]


grid_player = [["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [
    "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]]
# Display the grid

grid_top = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

ships = []
tf_array = []

points = int


def add_ship(o, p, x, y):
    ship = []
    ship.append(o)
    ship.append(p)
    ship.append(x)
    ship.append(y)
    ships.append(ship)


def display_player():
    y = 0
    n = 1
    print([0], grid_top)
    while y < 10:
        print([n], grid_player[y])
        y += 1
        n += 1


def display_ai():
    y = 0
    n = 1
    print([0], grid_top)
    while y < 10:
        print([n], grid_ai[y])
        y += 1
        n += 1


def y_detector(y):
    if y < 0:
        print("negative")
    elif y > 9:
        print("positive")


def down(x, y, piece):
    while piece > 0:
        grid_ai[y][x] = "x"
        piece -= 1
        y += 1


def right(x, y, piece):
    while piece > 0:
        grid_ai[y][x] = "x"
        piece -= 1
        x += 1


def AI_grid_init():
    tf_array = []
    r = 0
    p = 0
    for i in range(5):
        o = random.randint(1, 2)
        r += 1
        if r == 1 or r == 2:
            p = r + 1
        else:
            p = r

        if o == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            z = p + y
            while z > 9 or z < 0:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                z = p + y
            add_ship(p, "Vertical", x, y)
            down(z, y, p)
        elif o == 2:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            z = p + x
            while z > 9 or z < 0:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                z = p + x
            add_ship(p, "Horizontal", x, y)
            right(x, y, p)
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


def check_collision():
    p = int
    o = str
    x = int
    y = int
    section = 0
    for i in range(5):
        p = ships[section][0]
        o = ships[section][1]
        x = ships[section][2]
        y = ships[section][3]
        section += 1
        if o == "Horizontal":
            tf = bool
            end = p + x
            if "x" in grid_ai[y][x:end]:
                tf = True
                tf_array.append(tf)
            else:
                tf = False
        elif o == "Vertical":
            tf = bool
            for i in range(p):
                if "x" in grid_ai[y][x]:
                    tf = True
                else:
                    y += 1
                    tf = False
            tf_array.append(tf)


def AI_checker():
    AI_grid_init()
    print(ships)
    check_collision()
    print(tf_array)
    if True in tf_array[0:4]:
        AI_grid_init()
        check_collision()
    else:
        display_ai()


AI_checker()
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
