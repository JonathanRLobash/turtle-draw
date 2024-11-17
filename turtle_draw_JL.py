import turtle
import math

filename = input("Enter file name: ")
print("File name is: " + filename)

TEXTFILENAME = 'turtle-draw.txt'
turtleDrawTextFile = open(TEXTFILENAME, 'r')
line = turtleDrawTextFile.readline()


window = turtle.Screen()
window.screensize(450, 450)

Bob = turtle.Turtle()
Bob.speed(10)

# Function to calculate the Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Function to calculate the total distance between multiple points
def total_distance(points):
    total = 0
    for i in range(1, len(points)):
        total += distance(points[i-1], points[i])
    return total

# Function to read points from the file
def read_points_from_file(TEXTFILENAME):
    points = []
    with open(TEXTFILENAME, 'r') as file:
        for line in file:
            line = line.strip()
            returnStrings = line.split()
            if len(returnStrings) == 1:
                Bob.penup()
            elif len(returnStrings) == 3:
                colors = returnStrings[0]
                x = int(returnStrings[1])
                y = int(returnStrings[2])
                
                Bob.color(colors)
                Bob.goto(x, y)
                Bob.pendown()
                points.append((x, y))  # Save the point for distance calculation
    return points

# Read points from the text file
points = read_points_from_file(TEXTFILENAME)

# Calculate the total distance
total = total_distance(points)
print(f"Total Distance: {total:.2f}")


Bob.penup()
Bob.goto(200, -250)
Bob.pendown()
Bob.write(f"Total Distance: {total:.2f}", align="center", font=("Arial", 10, "normal"))

input("Press Enter to close the window...")

turtle.bye()

print('End')