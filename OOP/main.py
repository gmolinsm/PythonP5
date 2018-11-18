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

    def origindist(self):
        return (self.pointx ** 2 + self.pointy ** 2) ** 0.5

    def distance(self, other):
        return((self.pointx - other.pointx)**2 + (self.pointy - other.pointy)**2)**0.5

    def __eq__(self, other):
        return (self.pointx == other.pointx) and (self.pointy == other.pointy)

    def __len__(self):
        return 0

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

    def __str__(self):
        return "<" + str(self.pointx) + "," + str(self.pointy) + ">"

    def __lt__(self, other):
        d1 = Point.origindist(self)
        d2 = Point.origindist(self)

        return d1 < d2

    def __gt__(self, other):
        return self.pointx > other.pointx and self.pointy > other.pointy


p1 = Point(1, 1)
p2 = Point(1, 1)

print(p1 == p2)

p1 = Point(7, 9)
p2 = Point(0, -1)

print(p1.pointx, p1.pointy, p2.getx(), p2.gety(), Point.number, dir(Point))

p1.setx(9)
print(p1.getx(), Point.number)

print(Point.distance(Point(0, 0), Point(1, 1)))

l = []
p = Point(1, 10)
l.append(p)
p = Point(1, 3)
l.append(p)
p = Point(5, 6)
l.append(p)

for p in l:
    print(p)


class fraction(object):
    def __init__(self, num, den):
        self.x = num
        self.y = den

    def __str__(self):
        return str(self.x) + "/" + str(self.y)

    def __add__(self, other):
        x = self.x * other.y + self.y * other.x
        y = self.y * other.y

        return fraction(x, y)


