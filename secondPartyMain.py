#Elliptic curve Project
#Programmed by Adam Bowers and Nick Hilbert
#This is the driver for first party in two party communication
#it reads in config from secondPartyConfig.cfg, sends its shared secret to second first, 
#recieves shared secret from first party,  and calculates final shared secret which it then outputs

from ecc import Ecc
from point import Point
from ff import inv
from dhec import DhecUser
import configparser
from communication import recInfo
from communication import sendInfo

def main():
    #read in config information and process
    config = configparser.RawConfigParser()
    config.read('secondPartyConfig.cfg')
    p = config.getint('runInfo','fieldMod') # field modulo p
    a = config.getint('runInfo','aVal')
    b  = config.getint('runInfo','bVal') # curve parameters
    genX = config.getint('runInfo','GeneratorX')
    genY = config.getint('runInfo','Generatory')
    G = Point(genX,genY) # generator point
    curve = Ecc(a, b, p)
    n = curve.getOrder(G) # ord(G)
    mySecret = DhecUser(curve, G,
                        config.getint('runInfo','generatorMult'))
    communicationIp = config.get('runInfo','otherIpAddress')
    communicationPort = config.getint('runInfo','otherPort')
    myIp = config.get('runInfo','myIpAddress')
    myPort = config.getint('runInfo','myPort')
    #generate shared secret
    toShare = mySecret.generatePublicKey().toString()
    sharedSecret = Point()
    #communicate with second party
    sendInfo( mySecret.generatePublicKey().toString(),communicationIp,communicationPort)
    recInfo(sharedSecret,myIp,myPort)
    #get final shared secret
    SharedSecretResult = mySecret.calculateSharedSecret(sharedSecret)
    print(SharedSecretResult.toString())


if __name__=="__main__":
    main()