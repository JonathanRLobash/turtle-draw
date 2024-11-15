import turtle
window = turtle.Screen()
window.screensize(450, 450)
"""
spiral = turtle.Turtle()
spiral.speed(10)

spiral.pencolor("purple")
for i in range(40):
    spiral.forward(i * 10)
    spiral.right(144)


turtle.done()
"""
TEXTFILENAME = 'turtle-draw.txt'

turtleDrawTextFile = open(TEXTFILENAME, 'r')
line = turtleDrawTextFile.readline()
while line:
    #print(line, end='')
    line = turtleDrawTextFile.readline()

    returnStrings = line.split()
    if( len(returnStrings) == 1):
        print(returnStrings [0])

print('End')