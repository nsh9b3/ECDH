#Elliptic curve Project
#Programmed by Adam Bowers and Nick Hilbert
#This is the driver for first party in two party communication
#it reads in config from firstPartyConfig.cfg, recieves shared secret from second party,
#sends its shared secret to second party, and calculates final shared secret which it then outputs

from ecc import Ecc
from point import Point
from ff import inv
from dhec import DhecUser
import configparser
    
def main():
    #read first party config
    config = configparser.RawConfigParser()
    config.read('firstPartyConfig.cfg')
    p = config.getint('runInfo','fieldMod') # field modulo p
    a = config.getint('runInfo','aVal')
    b  = int(config.get('runInfo','bVal'),16) # curve parameters
    genX = int(config.get('runInfo','GeneratorX'),16)
    genY = int(config.get('runInfo','Generatory'),16)
    G = Point(genX,genY) # generator point
    curve = Ecc(a, b, p)
    #n = curve.getOrder(G) # ord(G)
    firstSecret = DhecUser(curve, G,
                        config.getint('runInfo','generatorMult'))
    #read second party config
    config = configparser.RawConfigParser()
    config.read('secondPartyConfig.cfg')
    #assuming curve parameters are the same, so don't read those
    secondSecret = DhecUser(curve, G,
                        config.getint('runInfo','generatorMult'))
    #get final shared secret
    firstPartySharedSecretResult = firstSecret.calculateSharedSecret(secondSecret.generatePublicKey())
    secondPartySharedSecretResult = secondSecret.calculateSharedSecret(firstSecret.generatePublicKey())
    print("First  party got point " + firstPartySharedSecretResult.toString())
    print("second party got point " + secondPartySharedSecretResult.toString())

if __name__=="__main__":
    main()