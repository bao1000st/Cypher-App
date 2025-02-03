import numpy as np


class Hill:
    def encrypt(self, msg, C):
        if self.check_Key(C) == -1:
            return ""
        # Replace spaces with nothing
        msg = "".join([c for c in msg.replace(" ", "") if c.isalpha()])

        # Append zero if the messsage isn't divisble by 2
        len_check = len(msg) % 2 == 0
        if not len_check:
            msg += "0"
        # Populate message matrix
        P = self.create_matrix_of_integers_from_string(msg)
        # Calculate length of the message
        msg_len = int(len(msg) / 2)
        # Calculate P * C
        encrypted_msg = ""
        for i in range(msg_len):
            # Dot product
            row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]
            # Modulate and add 65 to get back to the A-Z range in ascii
            integer = int(row_0 % 26 + 65)
            # Change back to chr type and add to text
            encrypted_msg += chr(integer)
            # Repeat for the second column
            row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
            integer = int(row_1 % 26 + 65)
            encrypted_msg += chr(integer)
        return encrypted_msg

    def decrypt(self, encrypted_msg, C):
        if self.check_Key(C) == -1:
            return ""
        encrypted_msg = "".join(
            [c for c in encrypted_msg.replace(" ", "") if c.isalpha()]
        )
        # Inverse matrix
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 26
        multiplicative_inverse = self.find_multiplicative_inverse(determinant)
        C_inverse = C
        # Swap a <-> d
        C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
        # Replace
        C[0][1] *= -1
        C[1][0] *= -1
        for row in range(2):
            for column in range(2):
                C_inverse[row][column] *= multiplicative_inverse
                C_inverse[row][column] = C_inverse[row][column] % 26

        P = self.create_matrix_of_integers_from_string(encrypted_msg)
        msg_len = int(len(encrypted_msg) / 2)
        decrypted_msg = ""
        for i in range(msg_len):
            # Dot product
            column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]
            # Modulate and add 65 to get back to the A-Z range in ascii
            integer = int(column_0 % 26 + 65)
            # Change back to chr type and add to text
            decrypted_msg += chr(integer)
            # Repeat for the second column
            column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
            integer = int(column_1 % 26 + 65)
            decrypted_msg += chr(integer)
        if decrypted_msg[-1] == "0":
            decrypted_msg = decrypted_msg[:-1]
        return decrypted_msg

    def find_multiplicative_inverse(self, determinant):
        multiplicative_inverse = -1
        for i in range(26):
            inverse = determinant * i
            if inverse % 26 == 1:
                multiplicative_inverse = i
                break
        return multiplicative_inverse

    def check_Key(self, C):
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 26
        return self.find_multiplicative_inverse(determinant)

    def create_matrix_of_integers_from_string(self, string):
        # Map string to a list of integers a/A <-> 0, b/B <-> 1 ... z/Z <-> 25
        integers = [self.chr_to_int(c) for c in string]
        length = len(integers)
        M = np.zeros((2, int(length / 2)), dtype=np.int32)
        iterator = 0
        for column in range(int(length / 2)):
            for row in range(2):
                M[row][column] = integers[iterator]
                iterator += 1
        return M

    def chr_to_int(self, char):
        # Uppercase the char to get into range 65-90 in ascii table
        char = char.upper()
        # Cast chr to int and subtract 65 to get 0-25
        integer = ord(char) - 65
        return integer
