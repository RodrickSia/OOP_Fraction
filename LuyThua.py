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
        
        return 
    # Code the function to print
    def _is_negative(self, a, b):
        if a < 0 and b > 0:
            return True
        if a > 0 and b < 0:
            return True
        return False
    
    # Functions to calculate the shorten result
    # Do later
    def _nthPower(n:int, nth):
        return
    # Do later
    def _construct_shorten(LuyThua):
        
    def _is_preferable(exponent, power):
        return
    
    
    def to_string(self):
        return f"({self.exponent})^({self.power})"
    
    def to_string(self):
        return f"({self.exponent})^({self.power})"

            
            