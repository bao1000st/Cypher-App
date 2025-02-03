import string

BASE64_ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"


class Base64:
    def str_to_bin(self, string):
        result = ""
        for i in string:
            result += bin(ord(i))[2:].zfill(8)

        if len(result) % 6 > 0:
            length = 6 - len(result) % 6
            result += "".zfill(length)

        if len(result) % 16 > 0:
            length = 16 - len(result) % 16
            for i in range(len(result), len(result) + length):
                result += "N"

        return result

    def str_to_base64(self, string):
        result = ""
        for i in string:
            if i == "=":
                continue
            result += bin(BASE64_ALPHABET.find(i))[2:].zfill(6)
        return result[0 : len(result) - len(result) % 8 :]

    def encrypt(self, string):
        bin = self.str_to_bin(string)
        encrypt = ""
        for i in range(0, int(len(bin) / 6)):
            t = bin[0 + i * 6 : 6 + i * 6]
            if t == "NNNNNN":
                encrypt += "="
            else:
                encrypt += BASE64_ALPHABET[int(t, 2)]
        return encrypt

    def decrypt(self, string):
        base64 = self.str_to_base64(string)
        decrypt = ""
        for i in range(0, int(len(base64) / 8)):
            t = base64[0 + i * 8 : 8 + i * 8]
            decrypt += chr(int(t, 2))
        return decrypt
