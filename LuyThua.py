class LuyThua:
    # Class fraciton before printing 
    class Fraction:
        def __init__(self, numerator, denominator):
            self.numerator = int(numerator)
            self.denominator = int(denominator)
            # Handle case when numerator is zero
            # Handle case when denominator is zero
            # Normalize
            if self.denominator != 0 and self.numerator != 0: # Edge case for 0^0
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
            # Case of 0 ^ 0
        if self.exponent.numerator == 0 and self._is_negative(self.power.numerator, self.power.denominator):
            return
        if self.exponent.numerator == 0 and self.power.numerator == 0:
            return
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
            return
                        
        # Handle case of negative power
        if self._is_negative(self.power.numerator, self.power.denominator):
            self.exponent.numerator, self.exponent.denominator = self.exponent.denominator, self.exponent.numerator
            self.power.numerator = -self.power.numerator
       
        # Handle when the exponent is not in correct format of negative
        if self._is_negative(self.exponent.numerator, self.exponent.denominator):
            self.exponent.numerator = -(abs(self.exponent.numerator))
            self.exponent.denominator = (abs(self.exponent.denominator))                        

        # Handle case when the exponent can be reduced to power
        components = self._get_common_power(self.exponent.numerator, self.exponent.denominator)
        if not components:
            return
        first, second = self._construct_shorten(components)
        self._simplify_power(first, second)
        return
        

    
    def _is_negative(self, a, b):
        if a < 0 and b > 0:
            return True
        if a > 0 and b < 0:
            return True
        return False
    
    # Functions to calculate the shorten result
    # Get the common power
    def _get_common_power(self, a: int, b: int, constrain=100):
        for n in range(2, constrain):
            # Check for negative inputs
            if a < 0 or b < 0:
                # If n is even, skip this iteration since even roots of negatives are not real.
                if n % 2 == 0:
                    continue
                # For odd n, compute the real nth root manually.
                A = round(-((-a) ** (1/n))) if a < 0 else round(a ** (1/n))
                B = round(-((-b) ** (1/n))) if b < 0 else round(b ** (1/n))
            else:
                A = round(a ** (1/n))
                B = round(b ** (1/n))
                
            if A ** n == a and B ** n == b:
                return (A, B, n)
        return None
    
    # Constructin 2 components of the simplified verson
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
        # Rebinding the simplified version
    def _rebind(self, a, b, c, d):
        self.exponent.numerator = a
        self.exponent.denominator = b
        self.power.numerator = c
        self.power.denominator = d
    
    def _simplify_power(self, new_first: "Fraction", new_second: "Fraction"):
        # We have first and second as the new LuyThua and self as the old LuyThua
        
        new_string = f"{new_first.__str__()}^{new_second.__str__()}"
        
        if len(self.to_string()) > len(new_string):
            self._rebind(new_first.numerator, new_first.denominator, new_second.numerator, new_second.denominator)

        elif self.exponent.numerator > new_first.numerator:
            self._rebind(new_first.numerator, new_first.denominator, new_second.numerator, new_second.denominator)
        
        elif self.exponent.denominator > new_first.denominator:
            self._rebind(new_first.numerator, new_first.denominator, new_second.numerator, new_second.denominator)
        
        elif self.power.numerator > new_second.numerator:
            self._rebind(new_first.numerator, new_first.denominator, new_second.numerator, new_second.denominator)
        
        elif self.power.denominator > new_second.denominator:
            self._rebind(new_first.numerator, new_first.denominator, new_second.numerator, new_second.denominator)
    
    # To readable string
    def to_string(self):
        return f"({self.exponent})^({self.power})"
    
  

            
            