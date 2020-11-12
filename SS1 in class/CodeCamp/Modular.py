
#Find Greatest Common Devisor (Euclidean Algorithm)
def gcd(a,b):
    if a%b == 0:
        return b
    return gcd( b, a%b)

