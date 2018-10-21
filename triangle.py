import math
import re


def main():
    V1 = inputCoordinateVertex()
    V2 = inputCoordinateVertex()
    V3 = inputCoordinateVertex()
    size1 = distance(V1, V2)
    size2 = distance(V2, V3)
    size3 = distance(V3, V1)
    area = calcArea(size1, size2, size3)
    output_result(area)


def calcArea(a, b, c):
    sp = (a + b + c) / 2
    area = float(math.sqrt(sp * (sp - a) * (sp - b) * (sp - c)))
    return area


def distance(ver1, ver2):
    lenght = math.sqrt((ver1[0] - ver2[0])**2 + (ver1[1] - ver2[1])**2)
    return lenght


def output_result(area):
    area = round(area, 1)
    area = str(area)
    area = re.sub(r'\.[0]', '', area)
    print("Area of the triangle : ", area)


def inputCoordinateVertex():
    print("Coordinate for vertex:")
    try:
        vertexX = int(input("Enter the x coordinate of vertex: "))
    except ValueError:
        print("Incorrect input")
    try:
        vertexY = int(input("Enter the y coordinate of vertex: "))
    except ValueError:
        print("Incorrect input")
    return vertexX, vertexY


main()