class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def rect_area(self):
        return self.width * self.height
    def get_rectangle(self):
        rectangle = f'Rectangle ({self.x}, {self.y}, {self.width}, {self.height}),'
        return rectangle

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def circle_area(self):
        return self.radius ** 2 * 3.14
    def get_circle(self):
        circle = f'Circle ({self.x}, {self.y}, {self.radius}),'
        return circle

rect_1 = Rectangle(4, 13, 5, 10)
rect_2 = Rectangle(1, 2, 2, 5)
circle_1 = Circle(1, 1, 1)
circle_2 = Circle(2, 5, 10)

figures = [rect_1, rect_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Circle):
        print(figure.get_circle(), "area =", figure.circle_area())
    else:
        print(figure.get_rectangle(), "area =", figure.rect_area())


