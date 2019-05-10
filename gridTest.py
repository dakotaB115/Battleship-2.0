grid_row = ["o", "o", "o", "o", "x", "o", "o", "o", "o", "o"]

tf = bool
if "x" in grid_row[0:4]:
    tf = True
else:
    tf = False
print(tf)

grid_multi = [["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
              ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
              ["o", "o", "x", "o", "o", "o", "o", "o", "o", "o"],
              ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]]

y = 0
for i in range(4):
    if "x" in grid_multi[y][2]:
        tf = True
    else:
        y += 1
        tf = False
print(tf)

ships = []


def add_ship(p, x, y):
    ship = []
    ship.append(p)
    ship.append(x)
    ship.append(y)
    ships.append(ship)
    print(ships)


add_ship("horizontal", 0, 0)
