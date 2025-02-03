import re
from cipher.ngram_score import ngram_score
import pathlib

fitness = ngram_score(
    f"{pathlib.Path().resolve()}\cipher\quadgrams.txt"
)  # load our quadgram statistics


class Caesar:
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

    def break_caesar(self, ctext):
        # make sure ciphertext has all spacing/punc removed and is uppercase
        ctext = re.sub("[^A-Z]", "", ctext.upper())
        # try all possible keys, return the one with the highest fitness
        scores = []
        for i in range(26):
            scores.append((fitness.score(Caesar().decrypt(ctext, i)), i))
        return max(scores)
