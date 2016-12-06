from ecc import Ecc
from point import Point
from ff import inv
from dhec import DhecUser

p = 17 # field modulo p
a,b = 2,2 # curve parameters
G = Point(5,1) # generator point
curve = Ecc(a, b, p)
n = curve.getOrder(G) # ord(G)

Alice = DhecUser(curve, G, 9)
Bob = DhecUser(curve, G, 3)

AlicePub = Alice.generatePublicKey()
BobPub = Bob.generatePublicKey()

print AlicePub.toString()
print BobPub.toString()

AliceSharedKey = Alice.calculateSharedSecret(BobPub)
BobSharedKey = Bob.calculateSharedSecret(AlicePub)

print AliceSharedKey.toString()
print BobSharedKey.toString()