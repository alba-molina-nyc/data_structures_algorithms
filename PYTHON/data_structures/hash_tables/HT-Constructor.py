
class HashTable:
    # passing in the size, set the parameter to set the default in the event you do not pass it a number
    def __init__(self, size = 7):
        # we are setting the list data_map and all of those are going to contain none
        self.data_map = [None] * size
      
    # this is the hash method - what we pass the key to determine the address where we store that key value pair 
    def __hash(self, key):
        # initialize it to zero
        my_hash = 0
        # loop through letters in the key that we passed the hash method
        for letter in key:
            # and when we do, we are going to run this calculation here 
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

        
my_hash_table = HashTable()

my_hash_table.print_table()

# ord(letter) - gets the ask key number for each letter as we pass through it 
# multiply by 23 because of prime numbers
# real key is modules (%) which gives you the remainder when you divide 
# if you divide any number by 7, it will give you a remainder of 6, and 0-6 is exactly our address base
# once we calculate, we are going to get a number from 0-6 and that is our address we use to place the key value pair in the hash table


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

        
# my_hash_table = HashTable()

# my_hash_table.print_table()

