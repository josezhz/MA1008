import turtle

def tryIntInput(title, prompt, default=None, minval=0, maxval=None):
    while True:
        try:
            x = int(screen.numinput(title, prompt, default, minval, maxval))
            return x
        except:
            print("Please enter an INTEGER")
def tryFloatInput(title, prompt, default=None, minval=0, maxval=None):
    while True:
        try:
            x = float(screen.numinput(title, prompt, default, minval, maxval))
            return x
        except:
            print("Please enter a NUMBER")

screen = turtle.Screen()
screen.setup(550, 750)
screen.setworldcoordinates(-5, 0, 105, 150)
turtle.speed(0)
'''
beamType = tryIntInput("Beam Type", "Beam type:\n1. Simply supported\n2. Overhanging\n3. Cantilever\nPlease enter an INTEGER", None, 1, 1)
_L = tryFloatInput("Beam Length", "L(mm) =", 1000, 0)
loads = []
while True:
    n = len(loads) + 1
    print("n =", n)
    loadType = tryIntInput(f"Load #{n}", "Load type:\n1. Concentrated load\n2. Uniformly distributed load\n3. Bending moment\nPlease enter an INTEGER", None, 1, 1)
    if loadType == 1:
        _P = tryFloatInput(f"Load #{n}", "P(N) =")
        _x = tryFloatInput(f"Load #{n}", "x(mm) =", None, 0, _L)
        loads.append([loadType, _P, _x])
    elif loadType == 2:
        _w = tryFloatInput(f"Load #{n}", "w(N/m) =")
        _x1 = tryFloatInput(f"Load #{n}", "x1(mm) =", None, 0, _L)
        _x2 = tryFloatInput(f"Load #{n}", "x2(mm) =", None, _x1, _L)
        loads.append([loadType, _w, _x1, _x2])
    elif loadType == 3:
        _M = tryFloatInput(f"Load #{n}", "M(Nm) =")
        _x = tryFloatInput(f"Load #{n}", "x(mm) =", None, 0, _L)
        loads.append([loadType, _M, _x])
    if not tryIntInput(f"Add Load #{n+1}?", "1: Yes\n0: No", None, 0, 1):
        break
print("_L =", _L, "beamType =", beamType)
print("loads =", loads)

dataFile = open("data.txt", "w")
print(beamType, _L, file=dataFile)
for eachLoad in loads:
    print(" ".join(str(e) for e in eachLoad), file=dataFile)
dataFile.close()
'''

turtle.up()
turtle.goto(-5, 0)
turtle.down()
turtle.goto(105, 0)
turtle.goto(105, 150)
turtle.goto(-5, 150)
turtle.goto(-5, 0)

turtle.up()
turtle.goto(-5, 100)
turtle.down()
turtle.forward(110)
turtle.up()
turtle.goto(-5, 50)
turtle.down()
turtle.forward(110)
turtle.up()
turtle.goto(0, 123)
turtle.down()
turtle.fillcolor("lightgray")
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(4)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(4)
turtle.end_fill()
turtle.left(90)

dataFile = open("test.txt", "r")
lines = dataFile.readlines()
dataFile.close()
beamData = lines[0].split(" ")
loadsData = [l.split(" ") for l in lines[1:]]
print("beamData = ", beamData)
print("loadsData =", loadsData)

beamType = beamData[0]
if beamType == "1": # simply supported
    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(5)
    turtle.left(120)
    turtle.forward(5)
    turtle.left(120)
    turtle.forward(5)
    turtle.end_fill()
    turtle.right(120)

    turtle.up()
    turtle.forward(100)
    turtle.down()
    turtle.right(180)
    turtle.begin_fill()
    turtle.circle(2.5)
    turtle.end_fill()
    turtle.right(180)
elif beamType == "2":
    print("Overhanging beam under development")
elif beamType == "3":
    print("Cantilever beam under development")

def pLoad(x, y):
    loadPen = turtle.Turtle()
    loadPen.hideturtle()
    loadPen.color("black")
    loadPen.up()
    loadPen.goto(x, y)
    loadPen.down()
    loadPen.left(45)
    loadPen.forward(3)
    loadPen.back(3)
    loadPen.left(90)
    loadPen.forward(3)
    loadPen.back(3)
    loadPen.right(45)
    loadPen.forward(10)

pLoad(float(loadsData[0][2])/10, 127)

screen.exitonclick()
turtle.done()
