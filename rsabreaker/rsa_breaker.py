from key import Key
import input_lib as il
import break_tools as bt


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
        user_input = il.input_positive_integer()
        while (not bt.is_relative_prime(user_input, bt.phi(self.public_key.get_modulus()))) or user_input >= bt.phi(self.public_key.get_modulus()):
            print("Requirements for exponent has not been.\nPlease try again.")
            user_input = il.input_positive_integer()
        self.public_key.set_exponent(user_input)

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

    m = breaker.public_key.get_modulus()
    e_pu = breaker.public_key.get_exponent()
    e_pr = breaker.private_key.get_exponent()

    c = (20 ** e_pu) % m
    print((c ** e_pr) % m == 20)

