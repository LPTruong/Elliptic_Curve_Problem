from random import randint
from point import inverse_mod
from hashlib import sha1


class SignatureGenerator():
    def __init__(self, base_point, message, hash_func=sha1):
        self.G = base_point
        self.m = str(message)
        self.hash_func = hash_func
        
        assert self.G.order is not None and self.G.order > 0, "ERROR : wrong order"
        
        self._key_generate()
        result = self._sign_generate()
        while result is False:
            result = self._sign_generate()
        
        self.r, self.s = result
    
    def _key_generate(self):
        n = self.G.order
        self._d = randint(1, n - 1)
        print('d : ', self._d)
        self.Q = self._d * self.G
    
    def _sign_generate(self):
        G = self.G
        n = self.G.order
        d = self._d
        m = self.m
        hash_func = self.hash_func
        
        k = randint(1, n - 1)
        print('K được random bằng : ', k)
            
        kG = k * G
        print('k*G: ', kG)
        r = kG.x % n
        # print('r: ', r)
                
        if r == 0:
            return False
    
        k_inv = inverse_mod(k, n)
        # print('k^-1: ', k_inv)
        e = int(hash_func(m.encode('utf-8')).hexdigest(), 16)
        print('Thông điệp sau khi được hash bằng sha1 là e: ', e)
        s = (k_inv * (e + d * r)) % n
        s = int(s)
        # print('s: ', s)
        
        if s == 0:
            return False
        
        return r, s
    
    def get_public_key(self):
        return self.Q
    
    def get_signature(self):
        return self.r, self.s

