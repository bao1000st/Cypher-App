from itertools import cycle
import base64


class Xor:
    def __init__(self):
        self.k = ""

    def encrypt(self, data):
        try:
            xored = "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(self.k)))
            xored = xored.encode("ascii")
            xored = base64.encodebytes(xored).strip()
            return xored.decode("ascii")
        except:
            return ""

    def decrypt(self, data):
        try:
            data = base64.decodebytes(bytes(data, "ascii"))
            data = data.decode("ascii")
            xored = "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(self.k)))
            return xored
        except:
            return ""
