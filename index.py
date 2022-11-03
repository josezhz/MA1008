import turtle


def intInput(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except:
            print("!Please enter an INTEGER")


def floatInput(prompt):
    while True:
        try:
            x = float(input(prompt))
            return x
        except:
            print("!Please enter a NUMBER")


def limitedFloatInput(prompt, upperLimit, lowerLimit=0):
    while True:
        x = floatInput(prompt)
        if lowerLimit <= x <= upperLimit:
            return x
        else:
            print(f"!Input must be between {lowerLimit} and {upperLimit}")


L_ = floatInput("L(mm) = ")
while True:
    beamType = intInput("Beam type?\n1. Simply Supported\n2. Overhanging\n3. Cantilever\n")
    if beamType in [1, 2, 3]:
        break
    else:
        print("!Please choose from 1/2/3")
loads = []
while True:
    while True:
        loadType = intInput("Load type?\n1. concentrated load\n2. uniformly distributed load\n3. bending moment\n")
        if loadType == 1:
            P_ = floatInput("P(N) = ")
            x_ = limitedFloatInput("x(mm) = ", L_)
            loads.append([loadType, P_, x_])
            break
        elif loadType == 2:
            w_ = floatInput("w(N/m) = ")
            x1_ = limitedFloatInput("x1(mm) = ", L_)
            x2_ = limitedFloatInput("x2(mm) = ", L_, x1_)
            loads.append([loadType, w_, x1_, x2_])
            break
        elif loadType == 3:
            M_ = floatInput("M(Nm) = ")
            x_ = limitedFloatInput("x(mm) = ", L_)
            loads.append([loadType, M_, x_])
            break
    if input("Add another load? (y/n)").lower() == "n":
        break
print("L_ =", L_, "beamType =", beamType)
print("loads =", loads)

screen = turtle.Screen()
screen.setup(550, 750)
screen.setworldcoordinates(-5, 0, 105, 150)
turtle.speed(10)

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
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(4)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(4)
turtle.end_fill()

turtle.begin_fill()
turtle.right(30)
turtle.forward(5)
turtle.left(120)
turtle.forward(5)
turtle.left(120)
turtle.forward(5)
turtle.end_fill()

screen.exitonclick()
turtle.done()
