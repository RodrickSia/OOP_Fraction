class FractionPair:
    class Fraction:
        """Nested Fraction class for individual fractions"""
        def __init__(self, numerator, denominator):
            self.numerator = int(numerator)
            self.denominator = int(denominator)
            if self.denominator == 0:
                raise ValueError("Denominator cannot be zero")
            self._normalize()

        def _gcd(self, a, b):
            """Calculate Greatest Common Divisor"""
            a, b = abs(a), abs(b)
            while b:
                a, b = b, a % b
            return a

        def _normalize(self):
            """Reduce fraction and handle signs"""
            if self.denominator < 0:
                self.numerator = -self.numerator
                self.denominator = -self.denominator
            gcd = self._gcd(self.numerator, self.denominator)
            self.numerator //= gcd
            self.denominator //= gcd

        def __str__(self):
            return f"{self.numerator}/{self.denominator}"

    def __init__(self, fraction_string):
        """Initialize with a string containing two fractions separated by space"""
        # Split the input string into two fraction parts
        try:
            frac1_str, frac2_str = fraction_string.strip().split()
        except ValueError:
            raise ValueError("Input string must contain two fractions separated by a space")

        # Parse first fraction
        if '/' in frac1_str:
            num1, den1 = frac1_str.split('/')
        else:
            num1, den1 = frac1_str, '1'
        
        # Parse second fraction
        if '/' in frac2_str:
            num2, den2 = frac2_str.split('/')
        else:
            num2, den2 = frac2_str, '1'
            
        # Create two Fraction objects
        self.power = self.Fraction(num1, den1)
        self.exponent = self.Fraction(num2, den2)

    def __str__(self):
        """String representation of the pair"""
        return f"power: {self.power}, Exponent2: {self.exponenexponent}"

    def __repr__(self):
        return f"FractionPair('{self.power} {self.exponentexponent}')"