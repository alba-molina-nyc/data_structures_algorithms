
# when function two calls function three then function three gets added into the call stack
def funcThree():
    print('Three')

# when function one calls function two then function two gets added into the call stack 
def funcTwo():
    funcThree()
    print('Two')

# when function all it does is print out the string, once it runs that print statement then it calls on the funcTwo()
def funcOne():
    funcTwo()
    print('One')


# where we call function one
funcOne()

# def funcThree():
#     print('Three')

# def funcTwo():
#     funcThree()
#     print('Two')

# def funcOne():
#     funcTwo()
#     print('One')


# funcOne()