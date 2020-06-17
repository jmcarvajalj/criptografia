# Fast python code that first calls pow()
# then applies % operator
a = 3
b = 1000000000000000
p = (int)(1e9 + 7)

# Using direct fast method to compute
# (a ^ b) % p.
d = pow(a, b, p)
print("Resultado es",d)
#print(p)