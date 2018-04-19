class Key:
    def __init__(self, m, e):
        self.modulus = m
        self.exponent = e

    def set_modulus(self, m):
        self.modulus = m

    def set_exponent(self, e):
        self.exponent = e

    def get_modulus(self):
        return self.modulus

    def get_exponent(self):
        return self.exponent
