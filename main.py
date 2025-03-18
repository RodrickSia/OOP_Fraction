from LuyThua import LuyThua
import decimal

def main():
    testing = ["445/2873 0/1"]
    for test in testing:
        print(LuyThua(test).to_string())
   
    # Create Decimal objects
    exp_decimal = decimal.Decimal("3.14")
    pow_decimal = decimal.Decimal("2.718")

    # Use as_integer_ratio() to get numerator and denominator tuples
    print(LuyThua(exp_decimal, pow_decimal).to_string())

    # Create Fraction objects using LuyThua's inner Fraction class
    fraction1 = LuyThua.Fraction(2, 273)
    fraction2 = LuyThua.Fraction(3, 58)

    print(LuyThua(fraction1, fraction2).to_string())
    print(LuyThua().to_string())

main()
