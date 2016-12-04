import point,ff

def ecc():
    def __init__(self, a, b, p):
        this.curve = curve
        this.a = a
        this.b = b
        this.p = p

    def add(self, p1, p2):
        if p1.isZero():
            return p2
        if p2.isZero():
            return p1
        if p1.x == p2.x and p1.y == 0 and p1.isEqual(p2):
            return point(0,0)
        if p1.x == p2.x and p1.y != 0 and not p1.isEqual(p2):
            return point(0,0)
        if p1.x == p2.x and p1.y == 0 and p1.isEqual(p2):
            s = ((3 * p1.x * p1.x + self.a) * ff.inv(2 * p1.y, self.p)) % self.p
            r = point(0,0)
            r.x = (s * s - 2 * p1.x) % self.p
            r.y = (s * (p1.x - r.x) - p1.y) % self.p
            return r
        else:
            s = ((p1.y - p2.y) * ff.inv(p1.x - p2.x, self.p)) % self.p
            r = point(0,0)
            r.x = (s * s - (p1.x + p2.x)) % self.p
            r.y = (s * (p1.x - r.x) - p1.y) % self.p
            return r

    def mul(self, p1, n):
        q = p1
        for i in range(1, n):
            q = self.add(q, p1)

        return q
