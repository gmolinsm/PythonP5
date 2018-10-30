class Point(object):
    number = 2

    def __init__(self, x, y):
        self.pointx = x
        self.pointy = y

    def getx(self):
        return self.pointx

    def gety(self):
        return self.pointy

    def setx(self, x):
        self.pointx = x
        Point.number += 1
    def sety(self, y):
        self.pointy = y


p1 = Point(7,9)
p2 = Point(0,-1)

print(p1.pointx, p1.pointy, p2.getx(), p2.gety(), Point.number, dir(Point))

p1.setx(9)
print(p1.getx(), Point.number)