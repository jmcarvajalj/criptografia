# Python code to demonstrate naive
# method to compute gcd ( Euclidean algo )


def computeGCD(x, y):
    while (y):
        x, y = y, x % y

    return abs(x)

a= 6
b= 59
print("a=",a,"\nb=",b,"\ngcd(a,b)=",computeGCD(a, b))