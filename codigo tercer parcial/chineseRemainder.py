# A Python3 program to demonstrate
# working of Chinise remainder Theorem

# k is size of num[] and rem[].
# Returns the smallest number x
# such that:
# x % num[0] = rem[0],
# x % num[1] = rem[1],
# ..................
# x % num[k-2] = rem[k-1]
# Assumption: Numbers in num[]
# are pairwise coprime (gcd for
# every pair is 1)
import math
import lcm2


def findMinX(num, rem, k):
    x = 1 # Initialize result

    # As per the Chinise remainder
    # theorem, this loop will
    # always break.
    while (True):

        # Check if remainder of
        # x % num[j] is rem[j]
        # or not (for all j from
        # 0 to k-1)
        j = 0
        while (j < k):
            if (x % num[j] != rem[j]):
                break
            j += 1

        # If all remainders
        # matched, we found x
        if (j == k):
            return x

        # Else try next numner
        x += 1

    # Driver Code

#modulos
num = [2, 3, 4, 5, 6, 7]
#residuos
rem = [1, 1, 1, 1, 1, 0]
k = len(num)
N = math.prod(num)
print("la soulucion de x mas pequeña es", findMinX(num, rem, k),"mod(",lcm2.lcm,")")
#para hallar la solucion general modificar el arreglo l en lcm2.py haciendolo igual al arreglo
#num de este programa
print("la solucion general es", lcm2.lcm,"* n +",findMinX(num, rem, k), "en n pertenece a Z (sin modulo)" )
print("N es igual a", N)
print(findMinX(num, rem, k),"+",N,"es solucion,",findMinX(num, rem, k),"+ 2*",N,"es solucion, etc..")
print(findMinX(num, rem, k),"-",N,"es solucion,",findMinX(num, rem, k),"- 2*",N,"es solucion, etc..")

# This code is contributed by mits
