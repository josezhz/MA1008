import turtle

def tryIntInput(title, prompt, default=None, minval=None, maxval=None):
    while True:
        try:
            x = int(screen.numinput(title, prompt, default, minval, maxval))
            return x
        except:
            print("Please enter an INTEGER")
def tryFloatInput(title, prompt, default=None, minval=None, maxval=None):
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

def getData():
    beamType = tryIntInput("Beam Type", "Beam type:\n1. Simply supported\n2. Overhanging\n3. Cantilever\nPlease enter an INTEGER", None, 1, 3)
    _L = tryFloatInput("Beam Length", "L(mm) =", None, 0)
    beamData = [beamType, _L]
    if beamType == 2:
        _x_B = tryFloatInput("Support Position", "x_B(mm) =", None, 0, _L)
        beamData.append(_x_B)
    loads = []
    while True:
        n = len(loads) + 1
        loadType = tryIntInput(f"Load #{n}", "Load type:\n1. Concentrated load\n2. Uniformly distributed load (under development)\n3. Bending moment (under development)\nPlease enter an INTEGER", 1, 1, 1)
        if loadType == 1:
            _P = tryFloatInput(f"Load #{n}", "(+ve: upwards)\nP(N) =")
            _x = tryFloatInput(f"Load #{n}", "x(mm) =", None, 0, _L)
            loads.append([loadType, _P, _x])
        elif loadType == 2:
            _w = tryFloatInput(f"Load #{n}", "(+ve: upwards)\nw(N/m) =")
            _x1 = tryFloatInput(f"Load #{n}", "x1(mm) =", None, 0, _L)
            _x2 = tryFloatInput(f"Load #{n}", "x2(mm) =", None, _x1, _L)
            loads.append([loadType, _w, _x1, _x2])
        elif loadType == 3:
            _M = tryFloatInput(f"Load #{n}", "(+ve: clockwise)\nM(Nm) =")
            _x = tryFloatInput(f"Load #{n}", "x(mm) =", None, 0, _L)
            loads.append([loadType, _M, _x])
        if not tryIntInput(f"Add Load #{n+1}?", "1: Yes\n0: No", None, 0, 1):
            break

    dataFile = open("data.txt", "w")
    print(" ".join(str(e) for e in beamData), file=dataFile)
    for eachLoad in loads:
        print(" ".join(str(e) for e in eachLoad), file=dataFile)
    dataFile.close()
getData()

dataFile = open("data.txt", "r")
lines = dataFile.readlines()
dataFile.close()

beamData = [float(e) for e in lines[0].split(" ")]
print("beam data:", beamData)
L = beamData[1]
beamType = beamData[0]
if beamType in [1, 2]: # Simply Supported & Overhanging
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
elif beamType == 3: # Cantilever
    turtle.up()
    turtle.goto(100, 175)
    turtle.down()
    for i in range(175, 125, -5):
        turtle.goto(100, i)
        turtle.goto(105, i - 5)
        turtle.goto(100, i)
    turtle.goto(100, 125)

pLoadsData = []
wLoadsData = []
mLoadsData = []
for line in lines[1:]:
    loadData = [float(e) for e in line.split(" ")]
    if loadData[0] == 1: pLoadsData.append(loadData[1:])
    elif loadData[0] == 2: wLoadsData.append(loadData[1:])
    elif loadData[0] == 3: mLoadsData.append(loadData[1:])
if beamType in [1, 2]:
    F_B = -(sum(p[0]*p[1] for p in pLoadsData) + sum(w[0]*(w[2]-w[1])/1000*(w[1]+w[2])/2 for w in wLoadsData) + sum(-m[0]*1000 for m in mLoadsData)) / beamData[2 if beamType == 2 else 1]
    print("F_B =" , F_B)
    F_A = -sum(p[0] for p in pLoadsData) + sum(w[0]*((w[2]-w[1])/1000) for w in wLoadsData) - F_B
    print("F_A =", F_A)
    pLoadsData.append([F_A, 0])
    pLoadsData.append([F_B, L if beamType == 1 else beamData[2]])
elif beamType == 3:
    F_R = -sum(p[0] for p in pLoadsData)
    M_R = -sum(p[0]*(L-p[1]) for p in pLoadsData)/1000
    pLoadsData.append([F_R, L])
    pLoadsData.append([0, 0])
    mLoadsData.append([M_R, L])
def getIndex1(aList):
    return aList[1]
pLoadsData.sort(key=getIndex1)
def drawPLoad(p):
    P = p[0]
    x = p[1]
    loadPen = turtle.Turtle()
    loadPen.hideturtle()
    loadPen.up()
    if P < 0:
        loadPen.goto(x/L*100, 162)
        loadPen.right(90)
        loadPen.showturtle()
        loadPen.down()
        loadPen.write("{:.1f}".format(-P)+"N", align="center")
        loadPen.forward(10)
    elif P > 0:
        loadPen.goto(x/L*100, 134)
        loadPen.write("{:.1f}".format(P)+"N", align="center")
        loadPen.left(90)
        loadPen.showturtle()
        loadPen.forward(4)
        loadPen.down()
        loadPen.forward(10)
def drawWLoad(w):
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
def drawMLoad(m):
    M = m[0]
    xcor = m[1]/L*100
    loadPen = turtle.Turtle()
    loadPen.hideturtle()
    loadPen.up()
    loadPen.goto(xcor, 149.5)
    loadPen.begin_fill()
    loadPen.circle(.5)
    loadPen.end_fill()
    loadPen.goto(xcor, 148)
    loadPen.write("{:.1f}".format(M)+"Nm", align="right")
    if M < 0:
        loadPen.goto(xcor, 145)
        loadPen.down()
        loadPen.circle(5, 180)
    elif M > 0:
        loadPen.goto(xcor, 155)
        loadPen.left(180)
        loadPen.down()
        loadPen.circle(5, -180)
        loadPen.left(180)
    loadPen.showturtle()
for p in pLoadsData:
    drawPLoad(p)
for w in wLoadsData:
    drawWLoad(w)
for m in mLoadsData:
    drawMLoad(m)

print("P loads data:", pLoadsData)
print("w loads data:", wLoadsData)
print("M loads data:", mLoadsData)
'''
# Calculating V & M using generalised function
def return0IfNegative(x):
    return 0 if x < 0 else x
def calculateV(x):
    V = 0
    for p in pLoadsData:
        if p[1] < x: V -= p[0]
    for w in wLoadsData:
        V -= w[0]*return0IfNegative(x-w[1])/1000 - w[0]*return0IfNegative(x-w[2])/1000
    return V
def calculateM(x):
    M = 0
    for p in pLoadsData:
        M -= p[0]*return0IfNegative(x-p[1])/1000
    for w in wLoadsData:
        M -= w[0]/2*(return0IfNegative(x-w[1])/1000)**2 - w[0]/2*(return0IfNegative(x-w[2])/1000)**2
    return M
'''
# Shear Force Diagram
V0 = F_A if beamType in [1, 2] else 0
def plotSFD():
    # calculate Vmax & Vmin
    V, Vmax, Vmin = V0, V0, V0
    for p in pLoadsData[1:]:
        V += p[0]
        if V > Vmax: Vmax = V
        if V < Vmin: Vmin = V
    print("Vmax Vmin =", Vmax, Vmin)
    Vrange = Vmax-Vmin
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
    ycor_o = -Vmin/Vrange*50 + 65
    sfd_x = turtle.Turtle()
    sfd_x.up()
    sfd_x.goto(0, ycor_o-2)
    sfd_x.write(0, align="right")
    sfd_x.goto(0, ycor_o)
    sfd_x.down()
    for p in pLoadsData[1:]:
        x = p[1]
        xcor = x/L*100
        sfd_x.goto(xcor, ycor_o)
        sfd_x.goto(xcor, ycor_o+0.5)
        sfd_x.goto(xcor, ycor_o-0.5)
        sfd_x.goto(xcor, ycor_o)
        sfd_x.write(x, align="right")
    sfd_x.goto(100, ycor_o)
    sfd_x.goto(100, ycor_o+0.5)
    sfd_x.goto(100, ycor_o-0.5)
    sfd_x.goto(100, ycor_o)
    sfd_x.write(L, align="right")
    sfd_x.goto(103, ycor_o)
    sfd_x.write("x/mm")
    # SFD
    sfd = turtle.Turtle()
    sfd.up()
    sfd.hideturtle()
    sfd.goto(0, V0/Vrange*50+ycor_o)
    sfd.down()
    V = V0
    for p in pLoadsData[1:]:
        xcor = p[1]/L*100
        sfd.goto((sfd.xcor()+xcor)/2, sfd.ycor())
        sfd.write("{:.1f}".format(V), align="center")
        sfd.goto(xcor, sfd.ycor())
        V += p[0]
        sfd.goto(xcor, V/Vrange*50 + ycor_o)
plotSFD()

# Bending Moment Diagram
def plotBMD():
    # calculate Mmax & Mmin
    V = V0
    M, Mmax, Mmin = 0, 0, 0
    for i in range(len(pLoadsData)-1):
        M += V*(pLoadsData[i+1][1]-pLoadsData[i][1])/1000
        if M > Mmax: Mmax = M
        if M < Mmin: Mmin = M
        V += pLoadsData[i+1][0]
    print("Mmax Mmin =", Mmax, Mmin)
    Mrange = Mmax - Mmin
    # vertical axis
    bmd_y = turtle.Turtle()
    bmd_y.up()
    bmd_y.left(90)
    bmd_y.goto(0, 3)
    bmd_y.down()
    bmd_y.goto(0, 57)
    bmd_y.write("M/Nm", align="right")
    bmd_y.forward(1)
    # horizontal axis
    ycor_o = -Mmin/Mrange*50 + 5
    bmd_x = turtle.Turtle()
    bmd_x.up()
    bmd_x.goto(0, ycor_o-2)
    bmd_x.write(0, align="right")
    bmd_x.goto(0, ycor_o)
    bmd_x.down()
    for p in pLoadsData[0 if beamType == 3 else 1:]:
        x = p[1]
        xcor = x/L*100
        bmd_x.goto(xcor, ycor_o)
        bmd_x.goto(xcor, ycor_o+0.5)
        bmd_x.goto(xcor, ycor_o-0.5)
        bmd_x.goto(xcor, ycor_o)
        bmd_x.write(x, align="right")
    bmd_x.goto(100, ycor_o)
    bmd_x.goto(100, ycor_o+0.5)
    bmd_x.goto(100, ycor_o-0.5)
    bmd_x.goto(100, ycor_o)
    bmd_x.write(L, align="right")
    bmd_x.goto(103, ycor_o)
    bmd_x.write("x/mm")
    # BMD
    bmd = turtle.Turtle()
    bmd.up()
    bmd.hideturtle()
    bmd.goto(0, ycor_o)
    bmd.down()
    V = V0
    M = 0
    for i in range(len(pLoadsData)-1):
        xcor = pLoadsData[i+1][1]/L*100
        M += V*(pLoadsData[i+1][1]-pLoadsData[i][1])/1000
        ycor = M/Mrange*50 + ycor_o
        bmd.goto(xcor, ycor)
        bmd.goto(xcor, ycor-0.4)
        bmd.begin_fill()
        bmd.circle(0.4)
        bmd.end_fill()
        bmd.goto(xcor, ycor)
        Vnext = V + pLoadsData[i+1][0]
        if M > 0:
            textAlign = "center"
            if V > 0 and Vnext > 0: textAlign = "right"
            elif V < 0 and Vnext < 0: textAlign = "left"
            bmd.write("{:.1f}".format(M), align=textAlign)
        elif M < 0:
            textAlign = "center"
            if V < 0 and Vnext < 0: textAlign = "right"
            elif V > 0 and Vnext > 0: textAlign = "left"
            bmd.up()
            bmd.goto(bmd.xcor(), bmd.ycor()-4)
            bmd.write("{:.1f}".format(M), align=textAlign)
            bmd.goto(bmd.xcor(), bmd.ycor()+4)
            bmd.down()
        V = Vnext
    if beamType == 3:
        bmd.goto(100, ycor_o)
plotBMD()

screen.exitonclick()
turtle.done()