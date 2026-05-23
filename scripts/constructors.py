class Circle:
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return 3.14 * self.rad ** 2

c1 = Circle(2)
print(c1.area())
