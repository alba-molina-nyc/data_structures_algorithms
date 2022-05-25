# defines function factorial and passes in (n)
def factorial(n):
    # checks if n = 1
    if n == 1:
        # if it is then return 1 
        return 1
        # this line below is where the function calls itself
    return n * factorial(n-1)


print(factorial(4))

# look at factorial vid again
# looking back at the call stack.py in this folder you can apply the same logic to this example
# you call factorial(4) and that gets added to the very bottom of the call stack
# then factorial(3) gets added next in the call stack
# then factorial(2) gets added next in the call stack
# then factorial(1) gets added LASTLY for this example in the call stack
# --
# then you go through the call stack and stacks start at the top so it would pop off all the factorials in order
# factorial(1)
# factorial(2)
# factorial(3)
# factorial(4) until we get to 24 which is the number we return 

# when it returns 1, it is going to start popping off the first factorial from the call stack


# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)


# print(factorial(4))
