class Affine:
    def __init__(self):
        self.die = 26
        self.key = tuple()

    def mode_inverse(self, x, m):
        for n in range(m):
            if (x * n) % m == 1:
                return n
            elif n == m - 1:
                return "Null"
            else:
                continue

    def encryptChar(self, char):
        char = char.upper()
        K1, K2, kI = self.key
        if char.isalpha():
            return chr((K1 * (ord(char) - 65) + K2) % self.die + 65)
        else:
            return char

    def decryptChar(self, char):
        char = char.upper()
        K1, K2, kI = self.key
        if char.isalpha():
            return chr(kI * ((ord(char) - 65) - K2) % self.die + 65)
        else:
            return char

    def encrypt(self, string):
        return "".join(map(self.encryptChar, string))

    def decrypt(self, string):
        return "".join(map(self.decryptChar, string))
