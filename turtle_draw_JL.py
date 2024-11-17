import turtle
window = turtle.Screen()
window.screensize(450, 450)
TEXTFILENAME = 'turtle-draw.txt'

filename = input("Enter file name:")
print("file name is: " + filename)
TEXTFILENAME=filename

Bob=turtle.Turtle()
Bob.speed(10)
turtleDrawTextFile = open(TEXTFILENAME, 'r')
line = turtleDrawTextFile.readline()
while line:
    #print(line, end='')
    line = turtleDrawTextFile.readline()

    returnStrings = line.split()
    if( len(returnStrings) == 1):
        Bob.penup()
    elif( len(returnStrings)==3):
        colors = returnStrings[0]
        x = int(returnStrings[1])
        y = int(returnStrings[2])

        Bob.color(colors)
        Bob.goto(x,y)
        Bob.pendown()

turtle.done()
turtleDrawTextFile.close()

print('End')