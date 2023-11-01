from abc import ABC , abstractclassmethod

class shape(ABC):
    @abstractclassmethod
    def printarea(self):
        return 0

class Rectangle(shape):
    type = "Rectangle"
    side = 4
    def __init__(self):
        self.length = 7
        self.breadth = 9
    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())




class Square(shape):
    type = "Square"
    
    def __init__(self):
        self.length = 9
        self.length = 9
    def printarea(self):
        return self.length * self.length

sqr1 = Square()
print(sqr1.printarea())

class Tringle(shape):
    type = "Tringle"

    def __init__(self):
        self.Base = 2
        self.Height = 6
    def printarea(self):
        return 1/2 * self.Base * self.Height

tri1 = Tringle()
print(tri1.printarea())

