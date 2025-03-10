def _get_common_power(a: int, b: int, constrain = 100):
    print(a, b)
    for n in range(2, constrain):
        A = round(a ** (1/n))
        B = round(b ** (1/n))
        if int(A**n) == a and int(B**n) == b:
            return (A, B, n)
    return None
print(_get_common_power(4, 9))