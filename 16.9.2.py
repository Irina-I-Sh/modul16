class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def rectangle_area(self):
        return self.length * self.width
    def get_rectangle(self):
        rect = f'Length = {self.length}, Width = {self.width},'
        return rect

rectangle_1 = Rectangle(5,3)

print(rectangle_1.get_rectangle(), "Area =", rectangle_1.rectangle_area())