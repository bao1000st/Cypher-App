from math import ceil


class Transposition:
    def encrypt_split(self, seq, key):
        return [seq[i : i + len(key)] for i in range(0, len(seq), len(key))]

    def encrypt(self, plaintext, key):
        plaintext = plaintext.replace(" ", "")

        # add numbers of z to string
        add_part = abs(ceil(len(plaintext) / len(key)) * len(key) - len(plaintext))
        if len(plaintext) % len(key) != 0:
            plaintext += "".join("z" for i in range(add_part))

        order = [[val, num] for num, val in enumerate(key)]
        ciphertext = ""

        for index in sorted(order):
            for part in self.encrypt_split(plaintext, key):
                try:
                    ciphertext += part[index[1]]
                except IndexError:
                    continue
        return ciphertext

    def decrypt_split(self, seq, key):
        n = ceil(len(seq) / len(key))
        return [seq[i : i + n] for i in range(0, len(seq), n)]

    def sort_order(self, order, key):
        result = []
        for c in key:
            for e in order:
                if c == e[0] and e[1] != -1:
                    result.append([e[0], e[1]])
                    e[1] = -1
                    break
        return result

    def decrypt(self, ciphertext, key):
        ciphertext = ciphertext.replace(" ", "")
        plaintext = ""
        for part in range(ceil(len(ciphertext) / len(key))):
            l = self.decrypt_split(ciphertext, key)
            order = self.sort_order(
                [[val, num] for num, val in enumerate(sorted(key))], key
            )
            for index in order:
                plaintext += l[index[1]][part]

        return plaintext
