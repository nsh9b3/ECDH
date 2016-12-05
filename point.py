class point:
    def __init__(self, x=0, y=0):
        self.x = x;
        self.y = y;

    def isEqual(self, p):
        if self.x == p.x:
            if self.y == p.y:
                return True;
        
        return False

    def isZero(self):
        if self.x == 0:
            if self.y == 0:
                return True

        return False

    def toString(self):
        return '({}, {})'.format(self.x, self.y)
