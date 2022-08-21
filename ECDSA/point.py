class PointOfEC():
    """
    Definition of Point in Elliptic Curve over Finite Fields
    and operation '+' and '*' of a point on the Curve.
    """
    
    def __init__(self, prime, alpha, beta, x, y, order=None):
        self.p = prime
        self.a = alpha
        self.b = beta
        self.r = order
        self.is_infinity = False
        
        if x is None and y is None:
            self.x = None
            self.y = None
            self.is_infinity = True
        elif x is not None and y is not None:
            self.x = x % prime
            self.y = y % prime
            assert is_on_curve(self), 'NOT include this point'
        else:
            assert False, 'ERROR : Inadequate initialize'
            
    def __str__(self):
        return 'Point : ( ' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, other):
        """
        Definition of '+' between a point and a other point.
        """
        
        if self.is_infinity:
            return other
        elif other.is_infinity:
            return self
        
        x1 = self.x
        y1 = self.y
        x2 = other.x
        y2 = other.y
        
        a = self.a
        b = self.b
        p = self.p
        r = self.r
        
        if x1 == x2 and ((y1 + y2) % p) == 0:
            return PointOfEC(p, a, b, None, None, r)
        elif x1 == x2:
            inv = inverse_mod(2 * y1, p)
            lam_numerator = (3 * x1 * x1 + a) % p
            neu_numerator = (-(x1 * x1 * x1) + a * x1 + 2 * b) % p
        else:
            inv = inverse_mod(x2 - x1, p)
            lam_numerator = (y2 - y1) % p
            neu_numerator = (y1 * x2 - y2 * x1) % p
        
        lam = (lam_numerator * inv) % p
        neu = (neu_numerator * inv) % p
        
        x3 = (lam * lam - x1 - x2) % p
        y3 = (-lam * x3 - neu) % p
        
        return PointOfEC(p, a, b, x3, y3, r)

    def __mul__(self, other):
        """
        Definition of '*' between a point and a scalar number.
        This method supported 'point * scalar'.
        """
        
        s = abs(other)
        
        p = self.p
        a = self.a
        b = self.b
        r = self.r
        
        if other == 0:
            return PointOfEC(p, a, b, None, None, r)
        
        result = PointOfEC(p, a, b, None, None, r)
        tmp = self
        while s != 0:
            if s % 2 == 1:
                result = result + tmp
            tmp = tmp + tmp
            s //= 2
        
        if other < 0:
            result = PointOfEC(p, a, b, result.x, -result.y, r)
        
        return result

    def __rmul__(self, other):
        """
        Definition of '*' between a point and a scalar number.
        This method supported 'scalar * point'.
        """
        return self * other


def search_order(point):
    order = 0
    i = 1
    while order == 0:
        check_point = i * point
        if check_point.is_infinity:
            order = i
            break
        i += 1

    assert order > 0, 'ERROR : order is not found'
    return order


def is_on_curve(point):
    x = point.x
    y = point.y
    a = point.a
    b = point.b
    p = point.p
    
    if (y * y) % p == ((x**3) + (a*x) + b) % p:
        result = True
    else:
        result = False
    
    return result


def inverse_mod(number, p):
    inv_element = -1
    for i in range(p):
        if (number * i) % p == 1:
            inv_element = i
            break

    return inv_element
