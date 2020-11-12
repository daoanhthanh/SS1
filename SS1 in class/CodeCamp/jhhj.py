def inverse_mod(a, m):
    for i in range(1,m):
        if ( m*i + 1) % a == 0:
            return ( m*i + 1) // a
    return None

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.
    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a


a = input("Input a number of \"a\": ")
b = input("Input a number of \"b\": ")


print("The Greatest Common Divisor of %s and %s is %s" % (a, b, gcd(a,b)))
print("The Modular inverses of %s modulo %s is %s" % (a, b, inverse_mod(a,b)))