class Vigenere:
    def __init__(self):
        self.n = 26
        self.k = ""

    def encrypt(self, plaintext):
        plaintext = plaintext.replace(" ", "")
        plaintext = plaintext.upper()
        self.k = self.k.upper()
        key_len = len(self.k)
        key_as_int = [ord(i) for i in self.k]
        plaintext_int = [ord(i) for i in plaintext]
        ciphertext = ""
        for i in range(len(plaintext_int)):
            if plaintext[i].isalpha():
                ciphertext += chr(
                    ((plaintext_int[i] + key_as_int[i % key_len]) % self.n) + 65
                )
            else:
                ciphertext += plaintext[i]
        return str(ciphertext)

    def decrypt(self, plaintext):
        plaintext = plaintext.replace(" ", "")
        plaintext = plaintext.upper()
        self.k = self.k.upper()
        key_len = len(self.k)
        key_as_int = [ord(i) for i in self.k]
        plaintext_int = [ord(i) for i in plaintext]
        ciphertext = ""
        for i in range(len(plaintext_int)):
            if plaintext[i].isalpha():
                ciphertext += chr(
                    ((plaintext_int[i] - key_as_int[i % key_len]) % self.n) + 65
                )
            else:
                ciphertext += plaintext[i]
        return ciphertext
