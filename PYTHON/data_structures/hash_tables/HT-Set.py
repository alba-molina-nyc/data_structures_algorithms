class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  
    
    # set key value pair inside the hash table, we pass in a key and a value
    def set_item(self, key, value):
    # figure out the address where we are going to store key value pair, in this method we pass in the address and this will compute the address
        index = self.__hash(key)
        # if the address is initialized to none
        if self.data_map[index] == None:
        # we set that equal to that empty list, we only do this if all the addresses are initialized to none, we can create that empty list
            self.data_map[index] = []
            # now we have that empty list created we can put the key value pair into the empty list at that index, we append that key value pair 
        self.data_map[index].append([key, value])
    
        
my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()


# class HashTable:
#     def __init__(self, size = 7):
#         self.data_map = [None] * size

#     def print_table(self):
#         for i, val in enumerate(self.data_map): 
#             print(i, ": ", val)
      
#     def __hash(self, key):
#         my_hash = 0
#         for letter in key:
#             my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
#         return my_hash  

#     def set_item(self, key, value):
#         index = self.__hash(key)
#         if self.data_map[index] == None:
#             self.data_map[index] = []
#         self.data_map[index].append([key, value])
    
        
# my_hash_table = HashTable()

# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)

# my_hash_table.print_table()

