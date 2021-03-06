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
from communication import recInfo
from communication import sendInfo
    
def main():
    #read in config information and process
    config = configparser.RawConfigParser()
    config.read('firstPartyConfig.cfg')
    p = config.getint('runInfo','fieldMod') # field modulo p
    a = config.getint('runInfo','aVal')
    b  = int(config.get('runInfo','bVal'),16) # curve parameters
    genX = int(config.get('runInfo','GeneratorX'),16)
    genY = int(config.get('runInfo','Generatory'),16)
    G = Point(genX,genY) # generator point
    curve = Ecc(a, b, p)
    print("Initialized parameters")
    #n = curve.getOrder(G) # ord(G)
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
    recInfo(sharedSecret,myIp,myPort)
    sendInfo( toShare,communicationIp,communicationPort)
    #get final shared secret
    SharedSecretResult = mySecret.calculateSharedSecret(sharedSecret)
    print(SharedSecretResult.toString())


if __name__=="__main__":
    main()