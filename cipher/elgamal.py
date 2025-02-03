from elgamal.elgamal import Elgamal, PublicKey, PrivateKey, CipherText


class Elgamalx:
    def create_keys(self):
        pb, pv = Elgamal.newkeys(64)

        with open("keys/elgamal/publickey.txt", "w") as f:
            f.write(str(pb.p) + "\n")
            f.write(str(pb.g) + "\n")
            f.write(str(pb.y) + "\n")
        with open("keys/elgamal/privatekey.txt", "w") as f:
            f.write(str(pv.p) + "\n")
            f.write(str(pv.x) + "\n")

    def encrypt(self, plaintext, publickey_file):
        try:
            with open(publickey_file, "r") as x:
                p, g, y = x.readlines()
                ct = Elgamal.encrypt(
                    plaintext.encode(), PublicKey(int(p), int(g), int(y))
                )
                return (ct.a, ct.b)
        except:
            return ""

    def decrypt(self, encrypted_msg, privatekey_file):
        try:
            a, b = encrypted_msg[1:-1].split(", ")
            with open(privatekey_file, "r") as y:
                p, x = y.readlines()
                dd = Elgamal.decrypt(
                    CipherText(int(a), int(b)), PrivateKey(int(p), int(x))
                )
                return dd.decode()
        except:
            return ""
