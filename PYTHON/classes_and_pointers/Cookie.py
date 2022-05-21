# class Cookie:
#     def __init__(self, color):
#         self.color = color

#     def get_color(self):
#         return self.color

#     def set_color(self, color):
#         self.color = color


# cookie_one = Cookie('green')
# cookie_two = Cookie('blue')

# print('Cookie one is', cookie_one.get_color())
# print('Cookie two is', cookie_two.get_color())

# cookie_one.set_color('yellow')

# print('\nCookie one is now', cookie_one.get_color())
# print('Cookie two is still', cookie_two.get_color())






class Cookie:
    # __init__ - this is the CONSTRUCTOR to initialize, notice the SELF being passed into the params - this is how you can tell a method apart from a function, if it has self then it is a method NOT a function
    # color is the param
    def __init__(self, color):
    # self applies to the particular instance we are creating
        self.color = color

    # this is another METHOD we are passing in on top of the CONSTRUCTOR
    def get_color(self):
        return self.color

    # this is another METHOD
    def set_color(self, color):
        self.color = color

# variable_name set it equal to the type Cookie we just created, and we are passing in the color "green" and that gets passed to the constructor AKA "__init__" and that creates the green cookie
# this is us creating the cookies
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

# this is us printing the cookies we just created 
print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

# classes are used for every single data structure
cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())
