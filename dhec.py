from ecc import Ecc

class DhecUser:
	def __init__(self, ecc, g, k):
		self.ecc = ecc
		self.g = g
		self.k = k

	def generatePublicKey(self):
		return  self.ecc.mul(self.g, self.k)

	def calculateSharedSecret(self, pub):
		return self.ecc.mul(pub, self.k)