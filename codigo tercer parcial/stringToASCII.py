# Python3 code to demonstrate working of
# Convert String list to ascii values
# using list comprehension + ord()

# initialize list
test_list = ['RSA es muy importante']


# printing original list
print("The original list : " + str(test_list))

# Convert String list to ascii values
# using list comprehension + ord()
res = [ord(ele) for sub in test_list for ele in sub]

# printing result
print("The ascii list is : " + str(res))
