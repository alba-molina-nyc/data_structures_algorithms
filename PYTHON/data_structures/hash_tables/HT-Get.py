class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    # pass it a key
    def get_item(self, key):
        # figure out index for that key we pass in 
        index = self.__hash(key)
        # we only want to look for washers if there are key value pairs in that address
        if self.data_map[index] is not None:
            # once we know there are items there, we can loop through them -- we are going through the list inside the key
            for i in range(len(self.data_map[index])):
                # i in the first iteration is 0 as we move through the list, so does bolts match that 0 iteration, if not then continue going through the for loop if it is a match then return it 
                if self.data_map[index][i][0] == key:
                   return self.data_map[index][i][1]
                   # if there is not a match then return a none
        return None
             

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))


# class HashTable:
#     def __init__(self, size = 7):
#         self.data_map = [None] * size
      
#     def __hash(self, key):
#         my_hash = 0
#         for letter in key:
#             my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
#         return my_hash  

#     def print_table(self):
#         for i, val in enumerate(self.data_map): 
#             print(i, ": ", val)
    
#     def set_item(self, key, value):
#         index = self.__hash(key)
#         if self.data_map[index] == None:
#             self.data_map[index] = []
#         self.data_map[index].append([key, value])
    
#     def get_item(self, key):
#         index = self.__hash(key)
#         if self.data_map[index] is not None:
#             for i in range(len(self.data_map[index])):
#                 if self.data_map[index][i][0] == key:
#                     return self.data_map[index][i][1]
#         return None
             

# my_hash_table = HashTable()

# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)

# print(my_hash_table.get_item('bolts'))
# print(my_hash_table.get_item('washers'))
# print(my_hash_table.get_item('lumber'))
