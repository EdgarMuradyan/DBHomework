
from abc import ABC, abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def printShape(self):
        pass


class Rectangle(Shape):
    width = 0
    length = 0

    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def printShape(self):
        print("Rectangle Width = ", self.width, "\n")
        print("Rectangle Length = ", self.length, "\n")

    def getWidth(self):
        return self.width

    def getLength(self):
        return self.length


class Square(Shape):
    side = 0

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

    def getSide(self):
        return self.side

    def printShape(self):
        print("Square in side ", self.side, "\n")


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def getRadius(self):
        return self.radius

    def printShape(self):
        print("Circle radius is ", self.radius, "\n")


def terminal():
    shapes = []

    while True:
        shape_type = input("Set shape type: Circle, Square, Rectangle (or 'exit' to finish): ")

        if shape_type.lower() == 'exit':
            break

        if shape_type == "Square":
            side = input("Set side size: ")
            square = Square(side)
            shapes.append(square)
        elif shape_type == "Circle":
            radius = input("Set radius size: ")
            circle = Circle(radius)
            shapes.append(circle)
        elif shape_type == "Rectangle":
            length = input("Set length size: ")
            width = input("Set width size: ")
            rectangle = Rectangle(length, width)
            shapes.append(rectangle)
        else:
            print("Invalid shape type. Please enter Circle, Square, or Rectangle.")

    for shape in shapes:
        shape.printShape()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    terminal()

    c1 = Circle(5)
    s1 = Square(5)
    r1 = Rectangle(4, 5)

    c1.printShape()
    s1.printShape()


