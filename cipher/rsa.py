from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class RSAX:
    def create_keys(self):
        keyPair = RSA.generate(2048)
        pubKey = keyPair.publickey()
        pubKeyPEM = pubKey.exportKey()
        with open("keys/rsa/receiver.pem", "w") as f:
            f.write(pubKeyPEM.decode("ascii"))

        privKeyPEM = keyPair.exportKey()

        with open("keys/rsa/private.pem", "w") as f:
            f.write(privKeyPEM.decode("ascii"))

    def encrypt(self, plaintext, publickey_file):
        try:
            pubKey = RSA.import_key(open(publickey_file).read())
            msg = bytes(str(plaintext), "utf-8")
            encryptor = PKCS1_OAEP.new(pubKey)
            encrypted = encryptor.encrypt(msg)
            return encrypted.decode("raw_unicode_escape")
        except:
            return ""

    def decrypt(self, encrypted_msg, privatekey_file):
        try:
            keyPair = RSA.import_key(open(privatekey_file).read())
            decryptor = PKCS1_OAEP.new(keyPair)
            decrypted = decryptor.decrypt(bytes(encrypted_msg, "raw_unicode_escape"))
            return decrypted.decode("utf-8")
        except:
            return ""
