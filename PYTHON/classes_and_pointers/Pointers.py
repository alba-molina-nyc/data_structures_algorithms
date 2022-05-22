# Integers
num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2)) 

# num 1 && num 2 point to the same number in memory


num2 = 22 

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2) 

# integers are IMMUTABLE they cannot be changed once you put them in memory

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))


# #####################################

# Dictionaries - 

dict1 = {
         'value': 11
        }

dict2 = dict1 

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

# dictionaries can be changed, they can continue to change to the same place and point to the same place in memory

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))


# you can also change what dictionaries point to, just use head equal to whatever you want it