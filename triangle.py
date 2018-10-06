import math


def distance(x1, y1, x2, y2):
    lenght = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return lenght


vertex1x = int(input("Enter the x coordinate of vertex1: "))
vertex1y = int(input("Enter the y coordinate of vertex1: "))
vertex2x = int(input("Enter the x coordinate of vertex2: "))
vertex2y = int(input("Enter the y coordinate of vertex2: "))
vertex3x = int(input("Enter the x coordinate of vertex3: "))
vertex3y = int(input("Enter the y coordinate of vertex3: "))

side1 = distance(vertex1x, vertex1y, vertex2x, vertex2y)
side2 = distance(vertex2x, vertex2y, vertex3x, vertex3y)
side3 = distance(vertex3x, vertex3y, vertex1x, vertex1y)

sp = (side1 + side2 + side3) / 2
area = float(math.sqrt(sp * (sp - side1) * (sp - side2) * (sp - side3)))
print("Area of the triangle :", area)
