# Python3 code to find solution of
# ax + by = n

# function to find the solution
# Python 3 program to check for solutions
# of diophantine equations
from math import gcd


# This function checks if integral
# solutions are possible
def isPossible(a, b, c):
    return (c % gcd(a, b) == 0)


# Driver Code
if __name__ == '__main__':

    # First example
    a = 3
    b = 6
    c = 9
    if (isPossible(a, b, c)):
        print("Possible")
    else:
        print("Not Possible")







