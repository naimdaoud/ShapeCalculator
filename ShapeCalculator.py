class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width (self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            picture = "Too big for picture."
        else:
            for i in range(self.height):
                picture = picture + "*"*self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        area1 = self.get_area()
        area2 = shape.get_area()
        return int(area1 / area2)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

rec = Rectangle(51, 8)
sq = Square(4)
print(rec.get_amount_inside(sq))
print(rec)
print(sq)
print(rec.get_picture())