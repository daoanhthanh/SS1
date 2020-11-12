n=26
#This will find Greatest common divisor (Euclidean Algorithm)
def gcd(a,n):
    while a:
        n,a = a, n%a 
    return n

#Determine how long the p is
quotation=[]
def _list(a,n):
    while a:
        quotation.append(n//a)
        n,a = a, n%a
    return quotation

# calculate t0
p = []
p0 = 0
p1 = 1
def cal():
    p.append(0)
    p.append(1)
    for i in range(2, len(quotation)+1):
        p.append((p[i-2] - p[i-1]*quotation[i-2])%n)
    return p

_list(15,26)
cal()
print(p[-1])
