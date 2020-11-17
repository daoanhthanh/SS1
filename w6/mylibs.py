import math 
# a^b = ? (MOD mod)
def find_congruence(a,b,mod):
    
    '''
        This part will return convertion from a number to its base
        In this problem I use base_2, so n = 2.
    '''
    arr = []
    def base_n(x,n):
        while x:                        
            arr.append(x%n)
            x,n = x//n, n
    base_n(b,2)             # convert b to binary: [1, 0, 0, 1, 0, 1, 0, 1, 1, 1]

    '''
        add mấy cái 2^0, 2^1, 2^2, 2^3,... vào array arr2
    '''
    arr2 =[]
    for i in range(len(arr)):
        arr2.append(arr[i]*math.pow(2,i))    # [1.0, 0.0, 0.0, 8.0, 0.0, 32.0, 0.0, 128.0, 256.0, 512.0]

    '''
        step 3
        t chẳng biết miêu tả như thế nào :v 
        đại loại là tính lần lượt từng cái 667^(2^...) rồi add vàO array product
    '''
    product = []
    for i in range(len(arr2)):
        sth = pow(a,int(arr2[i]),mod)
        product.append(sth)              # product == [667, 1, 1, 107, 1, 422, 1, 484, 852, 322]

    #final step, lời sao ý vậy :))))
    pro = 1
    for i in product:
        pro = (pro*i) % mod

    return pro

'''
    This part find greatest common divisor of the 2 number
'''
li = []
def find_gcd(a,b):
    while b:
        li.append(a%b)
        a,b = b,a%b
    return(li[-2])


q = [] 
p = []
p.append(0)
p.append(1)
def congruence(a,c,b):
    # make sure this equation is in correct form: a*x = c (mode b)
    if a > b:
        a = a%b

    while a:
        q.append(b//a)
        b,a = a, b%a
    
    for i in range(2,len(q)+1):
        p.append(p[i-2] - p[i-1]*q[i-2])
    
    if find_gcd(a,b) == 1:
        # how to make x0 > 0
        a=b
    
    return p[-1]

print("p array:",congruence(28,1,48))
print("quotation array:",q)