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
screen.setup(500, 750)
screen.setworldcoordinates(-10, 0, 110, 180)
turtle.speed(0)
'''
beamType = tryIntInput("Beam Type", "Beam type:\n1. Simply supported\n2. Overhanging\n3. Cantilever\nPlease enter an INTEGER", None, 1, 2) # 3 under devepment
_L = tryFloatInput("Beam Length", "L(mm) =", 1000, 0)
if beamType == 2:
    global _x_B
    _x_B = tryFloatInput("Support Position", "x_B(mm) =", None, 0, _L)
beamData = [beamType, _L]
if beamType == 2:
    beamData.append(_x_B)
loads = []
while True:
    n = len(loads) + 1
    print("n =", n)
    loadType = tryIntInput(f"Load #{n}", "Load type:\n1. Concentrated load\n2. Uniformly distributed load\n3. Bending moment\nPlease enter an INTEGER", 1, 1) # 2&3 under development
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
print(" ".join(str(e) for e in beamData), file=dataFile)
for eachLoad in loads:
    print(" ".join(str(e) for e in eachLoad), file=dataFile)
dataFile.close()
'''
def init():
    turtle.hideturtle()
    turtle.up()
    turtle.goto(-10, 0)
    turtle.down()
    turtle.goto(110, 0)
    turtle.goto(110, 180)
    turtle.goto(-10, 180)
    turtle.goto(-10, 0)

    turtle.up()
    turtle.goto(-10, 120)
    turtle.down()
    turtle.forward(120)
    turtle.up()
    turtle.goto(-10, 60)
    turtle.down()
    turtle.forward(120)
    turtle.up()
    turtle.goto(0, 148)
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
init()

dataFile = open("test.txt", "r")
lines = dataFile.readlines()
dataFile.close()

beamData = [float(e) for e in lines[0].split(" ")]
print("beam data:", beamData)
L = beamData[1]
beamType = beamData[0]
if beamType in [1, 2]: # simply supported & overhanging
    # Support A
    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(5)
    turtle.left(120)
    turtle.forward(5)
    turtle.left(120)
    turtle.forward(5)
    turtle.end_fill()
    turtle.right(120)
    turtle.write("A", align="right")
    # Support B
    turtle.up()
    turtle.forward(100 if beamType == 1 else beamData[2]/beamData[1]*100)
    turtle.down()
    turtle.right(180)
    turtle.begin_fill()
    turtle.circle(2.5)
    turtle.end_fill()
    turtle.right(180)
    turtle.write("B", align="right")
elif beamType == 3:
    print("Cantilever beam under development")

pLoadsData = []
wLoadsData = []
mLoadsData = []
for line in lines[1:]:
    loadData = [float(e) for e in line.split(" ")]
    if loadData[0] == 1: pLoadsData.append(loadData[1:])
    elif loadData[0] == 2: wLoadsData.append(loadData[1:])
    elif loadData[0] == 3: mLoadsData.append(loadData[1:])
pLoadsData.sort(key=lambda l: l[1])
def pLoad(p):
    loadPen = turtle.Turtle()
    loadPen.hideturtle()
    loadPen.up()
    loadPen.goto(p[1]/L*100, 162)
    loadPen.right(90)
    loadPen.showturtle()
    loadPen.down()
    loadPen.write(f"{p[0]}N", align="center")
    loadPen.forward(10)
def wLoad(w):
    loadPen1 = turtle.Turtle()
    loadPen1.hideturtle()
    loadPen1.up()
    loadPen1.goto(w[1]/L*100, 157)
    loadPen1.right(90)
    loadPen1.showturtle()
    loadPen1.down()
    loadPen1.forward(5)
    loadPen2 = turtle.Turtle()
    loadPen2.hideturtle()
    loadPen2.up()
    loadPen2.goto(w[1]/10, 157)
    loadPen2.right(90)
    loadPen2.showturtle()
    loadPen2.down()
    loadPen2.goto(w[2]/10, 157)
    loadPen2.forward(5)
    loadPen3 = turtle.Turtle()
    loadPen3.hideturtle()
    loadPen3.up()
    loadPen3.goto((w[1]+w[2])/20, 157)
    loadPen3.right(90)
    loadPen3.showturtle()
    loadPen3.down()
    loadPen3.write(f"{w[0]}N/m", align="center")
    loadPen3.forward(5)
for p in pLoadsData:
    pLoad(p)
for w in wLoadsData:
    wLoad(w)

F_B = (sum(p[0]*p[1] for p in pLoadsData) + sum(w[0]*((w[2]-w[1])/100)*((w[1]+w[2])/2) for w in wLoadsData)) / (beamData[2 if beamData[0] == 2 else 1])
print("F_B =" ,F_B)
F_A = sum(p[0] for p in pLoadsData) + sum(w[0]*((w[2]-w[1])/100) for w in wLoadsData) - F_B
print("F_A =", F_A)
pLoadsData.append([-F_B, L if beamType == 1 else beamData[2]])
pLoadsData.sort(key=lambda l: l[1])
print("P loads data:", pLoadsData)
print("w loads data:", wLoadsData)
print("M loads data:", mLoadsData)
V = F_A
Vmax, Vmin = F_A, F_A
for p in pLoadsData:
    V -= p[0]
    if V > Vmax: Vmax = V
    if V < Vmin: Vmin = V
print("Vmax =", Vmax)
print("Vmin =", Vmin)
Vrange = Vmax-Vmin

# Shear Force Diagram
def plotSFD():
    # vertical axis
    sfd_y = turtle.Turtle()
    sfd_y.up()
    sfd_y.left(90)
    sfd_y.goto(0, 63)
    sfd_y.down()
    sfd_y.goto(0, 117)
    sfd_y.write("V/N", align="right")
    sfd_y.forward(1)
    # horizontal axis
    sfd_o_y = -Vmin/Vrange*50 + 65
    sfd_x = turtle.Turtle()
    sfd_x.up()
    sfd_x.goto(0, sfd_o_y)
    sfd_x.down()
    sfd_x.write(0, align="right")
    for p in pLoadsData:
        x = p[1]
        sfd_x.goto(x/L*100, sfd_o_y)
        sfd_x.goto(x/L*100, sfd_o_y+1)
        sfd_x.goto(x/L*100, sfd_o_y-1)
        sfd_x.goto(x/L*100, sfd_o_y)
        sfd_x.write(x/L, align="right")
    sfd_x.goto(103, sfd_o_y)
    sfd_x.write("x/mm")
    # SFD
    sfd = turtle.Turtle()
    sfd.up()
    sfd.hideturtle()
    sfd.goto(0, 115)
    sfd.down()
    V = F_A
    for i in range(len(pLoadsData)):
        x = pLoadsData[i][1]/L*100
        sfd.forward((x-sfd.xcor())/2)
        sfd.write("{:.1f}".format(V), align="center")
        sfd.goto(x, 65+(V-Vmin)/Vrange*50)
        V -= pLoadsData[i][0]
        sfd.goto(x, 65+(V-Vmin)/Vrange*50)
plotSFD()

screen.exitonclick()
turtle.done()
