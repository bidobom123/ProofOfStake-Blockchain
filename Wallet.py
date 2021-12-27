from crypto.PublicKey import RSA
from BlockchainUtils import BlockchainUtils
class Wallet():
    def __init__(self):
        self.keypair = RSA.generate(2048)

    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
