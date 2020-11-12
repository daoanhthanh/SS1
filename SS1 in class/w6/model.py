import mylibs

user_sig = input("Enter yout signature:")

# Convert String to ASCII and add it to an array 
a_scii = []
for i in user_sig:
    a_scii.append(ord(i))

# Encrypt the signature
p = 42179
q = 30101
n = q*p
print("***********************************")
print("N is:", str(n))
z = (q-1)*(p-1)
print("***********************************")
print("Z is:", str(z))

# choose e
e = 0
for i in range(z, z//2, -1):
    
