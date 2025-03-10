import random
class LuyThua:
    # Class fraciton before printing 
    class Fraction:
        def __init__(self, numerator, denominator):
            self.numerator = int(numerator)
            self.denominator = int(denominator)
            # Handle case when numerator is zero
            # Handle case when denominator is zero
            # Normalize
            if self.denominator != 0:
                self._normalize()   
        def _gcd(self, a, b):
            a = abs(a)
            b = abs(b)
            while b:
                a, b = b, a % b
            return a
        def _normalize(self):
            # Handle when denominator is smaller than 0
            if self.denominator < 0:
                self.numerator = - self.numerator
                self.denominator = - self.denominator
            gcd = self._gcd(self.numerator, self.denominator)
            self.numerator = self.numerator // gcd
            self.denominator = self.denominator // gcd
        
        def __str__(self):
            return f"{self.numerator}/{self.denominator}"
    
    # Construct the LuyThua case
    def __init__(self, luy_thua_string):
        # Construct the 2 fraction
        f1, f2 = luy_thua_string.split()
        if '/' in f1:
            n1, d1 = f1.split('/')
        else:
            n1 = f1
            d1 = 1
        if '/' in f2:
            n2, d2 = f2.split('/')
        else:
            n2 = f2
            d2 = 2
        
        self.exponent = self.Fraction(n1, d1)
        self.power = self.Fraction(n2, d2)
        
        # Handle case of undefined
            # Case of 0 in denominator
        if self.exponent.denominator == 0 or self.power.denominator == 0:
            return
            # Case of negatvtive and even root
        if self._is_negative(self.exponent.numerator, self.exponent.denominator) and self.power.denominator % 2 == 0:
            return
        
        # Handle case for 0 of exponent 0/7 8/4 (0/1)^(1/1)
        if self.exponent.numerator == 0:
            self.exponent.numerator = 0
            self.exponent.denominator = 1
            self.power.numerator = 1
            self.power.denominator = 1            
            return

        # Handle case for 1
        if (self.power.numerator == 0 and self.power.denominator != 0) or (self.exponent.numerator == 1 and self.exponent.denominator == 1):
            self.exponent.numerator = 1
            self.exponent.denominator = 1
            self.power.numerator = 0
            self.power.denominator = 1
                        
        
        # Handle case of negative power
        if self._is_negative(self.power.numerator, self.power.denominator):
            self.exponent.numerator, self.exponent.denominator = self.exponent.denominator, self.exponent.numerator
            self.power.numerator = -self.power.numerator
               
        # Handle case when the exponent can be reduced to power
        components = self._get_common_power(self.exponent.numerator, self.exponent.denominator)
        if not components:
            return
        self._simplify_power(self)

        return 
    
    def _is_negative(self, a, b):
        if a < 0 and b > 0:
            return True
        if a > 0 and b < 0:
            return True
        return False
    
    # Functions to calculate the shorten result

    def _get_common_power(self, a: int, b: int, constrain = 100):
        for n in range(2, constrain):
            A = round(a ** (1/n))
            B = round(b ** (1/n))
            if A**n == a and B**n == B:
                return (A, B, n)
        return None
    
    """
    @staticmethod
    def _is_preferable(old: "LuyThua", new: "LuyThua"):
        # Check length
        if len(old.to_string()) > len(new.to_string):
            return True
        # Check value
        if old.exponent.numerator > new.exponent.numerator:
            return True
        if old.exponent.denominator > new.exponent.denominator:
            return True
        if old.power.numerator > new.power.numerator:
            return True
        if old.power.denominator > new.power.denominator:
            return True
        
        return False
    """
    def _construct_shorten(self, components: tuple) -> "LuyThua":
        a = components[0]
        b = components[1]
        reduction_index = components[2]
        c = self.power.numerator
        d = self.power.denominator
        first = self.Fraction(a,b)
        second = self.Fraction(c*reduction_index, d)
        return first, second
        
    
    # Function to handle reduction of power using the output of construct shorten
    def _rebind(self, a, b, c, d):
        self.exponent.numerator = a
        self.exponent.denominator = b
        self.power.numerator = c
        self.power.denominator = d
    def _simplify_power(self, new_first, new_second):
        # We have first and second as the new LuyThua and self as the old LuyThua
        new_string = f"{new_first.__str__()}^{new_second.__str__()}"
        if len(self.to_string()) > new_string:
            # Construct new 
        
        
    
    
    # To readable string
    def to_string(self):
        return f"({self.exponent})^({self.power})"
    
  

            
            