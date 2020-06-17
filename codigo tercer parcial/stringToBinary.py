# Python 3 program to convert
# string into binary string

# utility function
def strToBinary(s):
    bin_conv = []

    for c in s:
        # convert each char to
        # ASCII value
        ascii_val = ord(c)

        # Convert ASCII value to binary
        binary_val = bin(ascii_val)
        bin_conv.append(binary_val[2:])

    return (' '.join(bin_conv))


# Driver Code
if __name__ == '__main__':
    s = 'RSA es muy importante'
print("IMPORTANTE")
print("FIJESE QUE LA CODIFICACION SEA DE 8 BITS")
print(strToBinary(s))

# This code is contributed

