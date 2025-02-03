class Multiply:
    def __init__(self):
        self.die = 26
        self.key = 0

    def mode_inverse(self, x, m):
        for n in range(m):
            if (x * n) % m == 1:
                return n
            elif n == m - 1:
                return "Null"
            else:
                continue

    def encryptChar(self, char, key):
        if char.isalpha() == False:
            return char
        return chr((key * (ord(char) - 65)) % self.die + 65)

    def decryptChar(self, char, inverse_key):
        if char.isalpha() == False:
            return char
        return chr((inverse_key * (ord(char) - 65)) % self.die + 65)

    def encrypt(self, string):
        return "".join(self.encryptChar(i, self.key) for i in string.upper())

    def decrypt(self, string):
        inverse_key = self.mode_inverse(self.key, self.die)
        return "".join(self.decryptChar(i, inverse_key) for i in string.upper())
