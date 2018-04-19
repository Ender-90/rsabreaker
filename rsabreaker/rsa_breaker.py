from key import Key
import input_lib as il
import break_tools as bt
from math import gcd


class RSABreaker:
    def __init__(self):
        self.public_key = None
        self.private_key = None

    def set_public_key(self):
        self.public_key = Key(None, None)
        print("Set modulus of public key.")
        user_input = il.input_positive_integer()
        self.public_key.set_modulus(user_input)
        print("Set exponent of public key.")
        user_input = self.input_public_exponent()
        self.public_key.set_exponent(user_input)

    def input_public_exponent(self):
        tmp_exponent = il.input_positive_integer()

        while gcd(bt.phi(self.public_key.get_modulus()), tmp_exponent) != 1 or tmp_exponent >= bt.phi(self.public_key.get_modulus()):
            print("Requirements for exponent has not been.\nPlease try again.")
            tmp_exponent = il.input_positive_integer()

        return tmp_exponent

    def display_public_key(self):
        if self.public_key:
            print("Public Key.\n\nModulus: {0}.\nExponent: {1}".format(self.public_key.get_modulus(),
                                                                       self.public_key.get_exponent()))
        else:
            print("Public key has not been set. Please set it first")

    def display_private_key(self):
        if self.private_key:
            print("Private Key.\n\nModulus: {0}.\nExponent: {1}".format(self.private_key.modulus,
                                                                        self.private_key.exponent))
        else:
            print("There is no private key. Please set public key and break it to obtain private key.")

    def break_the_key(self):
        A = bt.phi(self.public_key.get_modulus())
        list_of_euclidean = bt.euclidean_algorithm(self.public_key.get_exponent(), A)
        inverse_list = bt.extended_euclidean_algorithm(list_of_euclidean)
        if len(inverse_list) % 2 == 1:
            self.private_key = Key(self.public_key.get_modulus(), inverse_list[-1][2] + A)
        else:
            self.private_key = Key(self.public_key.get_modulus(), inverse_list[-1][0])


if __name__ == "__main__":
    breaker = RSABreaker()
    breaker.set_public_key()
    breaker.display_public_key()
    breaker.display_private_key()

    breaker.break_the_key()
    breaker.display_private_key()

