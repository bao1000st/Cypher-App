class Rot13:
    def encrypt(self, message, key):
        message = message.replace(" ", "")
        result = ""

        for i in range(len(message)):
            c = message[i]
            if c.isalpha():
                if c.isupper():
                    result += chr((ord(c) + key - 65) % 26 + 65)
                else:
                    result += chr((ord(c) + key - 97) % 26 + 97)
            else:
                result += c
        return result

    def decrypt(self, message, key):
        message = message.replace(" ", "")
        result = ""

        for i in range(len(message)):
            c = message[i]
            if c.isalpha():
                if c.isupper():
                    result += chr((ord(c) - key - 65) % 26 + 65)
                else:
                    result += chr((ord(c) - key - 97) % 26 + 97)
            else:
                result += c
        return result
