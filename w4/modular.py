dividend = []
divisor = []
quotient = []
remainder = []
#--------------- Extended euclidean algorithm
p = [0,1]
#--------------- Find root
x0 =0;
root = []

#find gcd(a,n)
def gcd(a,n):
    dividend.append(n)
    divisor.append(a)
    q = n//a
    r = n%a
    quotient.append(q)
    remainder.append(r)

    index = 1
    while(True):
        dividend.append(divisor[index-1])
        divisor.append(remainder[index-1])

        q = dividend[index] // divisor[index]
        r = dividend[index] % divisor[index]
        quotient.append(q)

        if r == 0:
            remainder.append(r)
            break
        else:
            remainder.append(r)
            index += 1

    return remainder[len(remainder)-2]

#find the value r in gcd(a,n) = n.s+a.r
def r(n):
    q = quotient
    for i in range(2, len(q)+1):
        x = (p[i-2] - p[i-1]*q[i-2])%n
        p.append(x)
    return p[i]

#find set the root of equation
def modulo(a,b,n):
    d = gcd(a,n)
    if b%d==0:
        x0 = int(((r(n) * b)/d) % (n/d))
        root.append(x0)
        for i in range(1,d):
            x = int((x0 + i * n/d) % n)
            root.append(x)
        return root
    else:
        return "No root!"

def main():

    print("Find ax = b mod n")
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    n = int(input("Input c: "))
    print("\nEquation: {}x = {} mod {}".format(a,b,n))

    root = modulo(a,b,n)

    #-----------
    d = gcd(a,n)
    #-----------
    print("\n\t\tDividend\t\tDivisor\t\tQuotient\t\tRemainder")
    for i in range(len(dividend)):
       print("\t\t{}\t\t\t\t{}\t\t\t{}\t\t\t\t{}".format(dividend[i], divisor[i], quotient[i], remainder[i]))

    print("\nExtended Euclidean Algorithm")
    print("------------------------------------------------")

    # print the process of finding t by extended auclidean algorithm
    print("p[0] = 0\np[1] = 1")
    for i in range(2,len(p)):
        print("p[{}] = {}-{}x{} mod {} = {}".format(i, p[i-2], p[i-1],quotient[i-2], n, p[i]))
    # print the process of finding all root
    print("\nFinding the root processing")
    print("------------------------------------------------")
    #x0
    print("x[0] = {}x{}/{} mod ({}/{}) = {}".format(r(n), b, d, n, d, x0))
    #x
    for i in range(1, len(root)):
        print("x[{}] = {}+{}x{}/{} = {}".format(i, x0, i, n, d, root[i]))

    #print the set of all root
    print("\nSet of all roots")
    print("------------------------------------------------")
    print("Root = ", root)
main()