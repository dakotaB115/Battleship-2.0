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
    if "x" in grid_multi[2][y]:
        tf = True
    else:
        y += 1
        tf = False
print(tf)

