from crypto import Signature
from crypto.PublicKey import RSA
from crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils
class Wallet():
    def __init__(self):
        self.keypair = RSA.generate(2048)

    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
        signatureSchemeObject = PKCS1_v1_5.new(self.keypair)
        signature= signatureSchemeObject.sign(dataHash)
        return signature.hex()