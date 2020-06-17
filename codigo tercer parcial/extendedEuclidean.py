# Python program to demonstrate working of extended
# Euclidean Algorithm

# function for extended Euclidean Algorithm
def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


# Driver code
a= 272582563372
b= -541032959194
g, x, y = gcdExtended(a, b)
print("Extended Euclidean Algorithm (a=",a,",b=",b,")\ngcd(",a,",",b,")=",g,"\nx=",x,"\ny=",y)
print(a,"*",x,"+",b,"*",y,"=",g)
print("Ahora procedemos a hallar multiples soluciones para la ecuacion a*x + b*y = gcd(a,b)")
print("de esta manera a*(x*n) + b*(y*n) = gcd(a,b)*n")
#modificar n para probar todas las posibles soluciones de la ecuacion
n=3
print(a,"* (",x,"*",n,") +",b,"* (",y,"*",n,") =",g,"*",n)
print(a,"* (",x*n,") +",b,"* (",y*n,") =",g*n)
print(a*x*n,"+",b*y*n,"=",g*n)
print(a*x*n+b*y*n,"=",g*n)