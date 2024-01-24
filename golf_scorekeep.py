# Golf Scorekeep
par = int(input(f"       Please enter par: "))
strokes = int(input(f"Please enter strokes: "))

if strokes == (par + 1):
    if strokes == 2 and par == 1:
        print("Error")
    else:
        print("Bogey")
if strokes == par:
    print("Par")
if strokes == (par - 1):
    print("Birdie")
if strokes == (par - 2):
    print("Eagle")
if strokes > (par + 1):
    print("Error")
if strokes < (par - 2):
    print("Error")
try:
    int(par)
except:
    print("Error")
try:
    int(strokes)
except:
    print("Error")
