#In this case we not use 'Liskov substitution principle'

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side * self.side

def print_area(rectangle):
    print("El área del rectángulo es:", rectangle.area())

rectangle = Rectangle(4, 6)
square = Square(5)

print_area(rectangle)
print_area(square)

#In this case we use 'Liskov substitution principle'

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

def print_area(rectangle):
    print("El área del rectángulo es:", rectangle.area())

rectangle = Rectangle(4, 6)
square = Square(5)

print_area(rectangle)
print_area(square)
