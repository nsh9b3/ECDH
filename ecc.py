from point import point
from ff import inv

class ecc:
    # y^2 = x^3 + a * x + b
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        self.points = []
        self.order = -1

    def add(self, p1, p2):
        r = point(0,0)
        if p1.isZero():
            r = p2
        elif p2.isZero():
            r = p1
        elif p1.x == p2.x and p1.y == 0 and p1.isEqual(p2):            
            r = point(0,0)
        elif p1.x == p2.x and p1.y != 0 and not p1.isEqual(p2):
            r = point(0,0)
        elif p1.x == p2.x and p1.y != 0 and p1.isEqual(p2):
            s = ((3 * p1.x * p1.x + self.a) * inv(2 * p1.y, self.p)) % self.p
            r = point(0,0)
            r.x = (s * s - 2 * p1.x) % self.p
            r.y = (s * (p1.x - r.x) - p1.y) % self.p
        else:
            s = ((p1.y - p2.y) * inv(p1.x - p2.x, self.p)) % self.p
            r = point(0,0)
            r.x = (s * s - (p1.x + p2.x)) % self.p
            r.y = (s * (p1.x - r.x) - p1.y) % self.p

        return r

    def mul(self, p1, n):
        q = p1
        for i in range(1, n):
            q = self.add(q, p1)

        return q

    def findPoints(self):
        if self.points != []:
            return self.points
        squares = []
        sqrt = []
        for i in range(self.p):
            square = (i * i) % self.p
            if square not in squares:
                squares.append(square)
                sqrt.append(i)

        self.points = []
        for i in range(self.p):
            x = i % self.p
            y2 = (x * x * x + self.a * x + self.b) % self.p
            if y2 in squares:
                self.points.append(point(x, sqrt[squares.index(y2)]))
                self.points.append(point(x, -sqrt[squares.index(y2)]))

        return self.points

    def getOrder(self, p1):
        self.findPoints()
        accessPoints = []
        accessPoints.append(p1)
        nextPoint = self.mul(p1, 2)
        i = 3
        while(nextPoint not in accessPoints):
            accessPoints.append(nextPoint)
            nextPoint = self.mul(p1, i)
            if nextPoint.isZero():
                self.order = i
                break
            i = i + 1

        return self.order