from point import inverse_mod
from hashlib import sha1


class SignatureVerificator():
    def __init__(self, base_point, message, hash_func=sha1):
        self.G = base_point
        self.m = message
        self.hash_func = hash_func
        
    def verify_message(self, r, s, public_key):
        G = self.G
        m = self.m
        Q = public_key
        n = self.G.order
        hash_func = self.hash_func
        
        if r < 1 or r > n - 1 or s < 1 or s > n - 1:
            print('reject')
            return False
        
        e = int(hash_func(m.encode('utf-8')).hexdigest(), 16)
        w = inverse_mod(s, n)
        w = int(w)
        print('w: ', w)
        u1 = (e * w) % n
        print('u1: ', u1)
        u2 = (r * w) % n
        print('u2: ', u2)
        
        GQ = (u1 * G) + (u2 * Q)
        print('u1*G: ', u1 * G)
        print('u2*Q: ', u2 * Q)
        print('(u1 * G) + (u2 * Q):', GQ)
        v = GQ.x % n
        print('v: ', v)
        
        if v == r:
            print('accept')
            return True
        else:
            print('reject:last')
            return False


