#simple rsa implementation
class RSA:
    def __init__(self, p, q, e):
        self.e = e
        n = p*q
        self.n = n
        phi = (p-1) * (q-1)
        d = pow(e, -1, phi)
        self.d = d
    def encrypt(self, m):
        c = (m**self.e) % self.n
        return c
    def decrypt(self, c):
        m = (c**self.d) % self.n
        return m
