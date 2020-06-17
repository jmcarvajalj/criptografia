# https://repl.it/@billbuchanan/getprimen
import Crypto.Util.number

import sys
import random

bits=512

if (len(sys.argv)>1):
        bits=int(sys.argv[1])

print ("No of bits in prime is ",bits)
#Importante aca se puede cambiar para que p sea un numero arbitrario
#p=47
p=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print ("\nRandom n-bit Prime (p): ",p)
#Importante aca se puede cambiar para que e sea un numero arbitrario
#q=71
q=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print ("\nRandom n-bit Prime (q): ",q)

N=p*q

print ("\nN=p*q=",N)

PHI=(p-1)*(q-1)

print ("\nPHI (p-1)(q-1)=",PHI)
#Importante aca se puede cambiar para que e sea un numero arbitrario
#e=65537
#e=79
e = random.randrange(1, PHI)
print ("\ne=",e)
d=Crypto.Util.number.inverse(e,PHI)
print ("d=",d)

print ("\nCount of decimal digits (p): ",len(str(p)))
print ("Count of decimal digits (N): ",len(str(N)))
#MENSAJE A CIFRAR
M=120318432865665020932164951669796724115622230652005

print("\nlas llaves son: \n")
print("llave publica (e,N)")
print("e=",e,"\nN=",N)
print("\nllave privada (d,N)")
print("d=",d,"\nN=",N)
print ("\nRSA Message: ",M)
enc=pow(M,e,N)
print ("RSA Cipher(c=M^e mod N): ",enc)
dec = pow(enc,d,N)
print ("RSA Decipher (c^d mod N): ",dec)
