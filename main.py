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
beamType = tryIntInput("Beam Type", "Beam type:\n1. Simply supported\n2. Overhanging\n3. Cantilever\nPlease enter an INTEGER", None, 1, 2) # 3 under devepment
_L = tryFloatInput("Beam Length", "L(mm) =", 1000, 0)
loads = []
while True:
    n = len(loads) + 1
    print("n =", n)
    loadType = tryIntInput(f"Load #{n}", "Load type:\n1. Concentrated load\n2. Uniformly distributed load\n3. Bending moment\nPlease enter an INTEGER", None, 1, 2) # 3 under development
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

turtle.hideturtle()
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
beamData = [float(e) for e in lines[0].split(" ")]
pLoadsData = []
wLoadsData = []
mLoadsData = []
for line in lines[1:]:
    loadData = [float(e) for e in line.split(" ")]
    if loadData[0] == 1: pLoadsData.append(loadData[1:])
    elif loadData[0] == 2: wLoadsData.append(loadData[1:])
    elif loadData[0] == 3: mLoadsData.append(loadData[1:])
print("beam data:", beamData)
print("P loads data:", pLoadsData)
print("w loads data:", wLoadsData)
print("M loads data:", mLoadsData)

beamType = beamData[0]
if beamType == 1: # simply supported
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
elif beamType == 2:
    print("Overhanging beam under development")
elif beamType == 3:
    print("Cantilever beam under development")

def pLoad(x):
    loadPen = turtle.Turtle()
    loadPen.hideturtle()
    loadPen.up()
    loadPen.goto(x/10, 137)
    loadPen.right(90)
    loadPen.showturtle()
    loadPen.down()
    loadPen.forward(10)

def wLoad(x1, x2):
    loadPen1 = turtle.Turtle()
    loadPen1.hideturtle()
    loadPen1.up()
    loadPen1.goto(x1/10, 132)
    loadPen1.right(90)
    loadPen1.showturtle()
    loadPen1.down()
    loadPen1.forward(5)
    loadPen2 = turtle.Turtle()
    loadPen2.hideturtle()
    loadPen2.up()
    loadPen2.goto(x1/10, 132)
    loadPen2.right(90)
    loadPen2.showturtle()
    loadPen2.down()
    loadPen2.goto(x2/10, 132)
    loadPen2.forward(5)
    loadPen3 = turtle.Turtle()
    loadPen3.hideturtle()
    loadPen3.up()
    loadPen3.goto((x1+x2)/20, 132)
    loadPen3.right(90)
    loadPen3.showturtle()
    loadPen3.down()
    loadPen3.forward(5)


for p in pLoadsData:
    pLoad(p[1])
for w in wLoadsData:
    wLoad(w[1], w[2])



screen.exitonclick()
turtle.done()
