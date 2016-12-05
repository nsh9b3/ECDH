from ecc import ecc
from point import point
from ff import inv

p = 17 # field modulo p
a,b = 2,2 # curve parameters
G = point(16,-4) # generator point
curve = ecc(a, b, p)
n = curve.getOrder(G) # ord(G)

print 'order: {}'.format(n)