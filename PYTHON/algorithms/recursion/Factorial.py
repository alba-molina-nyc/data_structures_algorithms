# defines function factorial and passes in (n)
def factorial(n):
    # checks if n = 1
    if n == 1:
        # if it is then return 1 
        return 1
        # this line below is where the function calls itself
    return n * factorial(n-1)


print(factorial(4))

# so in the above example we are setting n = 4 
# so then it says is 4 = 1 no
# so then it will call the function again n * factoria(n-1)
# so then it will say 3 = 1 no
# until you get to 1 and then return 1 

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)


# print(factorial(4))
