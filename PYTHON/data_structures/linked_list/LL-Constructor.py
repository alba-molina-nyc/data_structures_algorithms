# a node in the LL has two values, think of a node in LL like a dictionary that contains value and also a next 
class Node:
    # __init__ how you tell it is a method and not a function
    def __init__(self, value):
        self.value = value
        self.next = None
        
# we are setting head and tail point to the new node we just created 
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        # first node
        self.head = new_node
        # last node
        self.tail = new_node
        # keeping track of the length 
        self.length = 1

 
my_linked_list = LinkedList(4)

print(my_linked_list.head.value)


                                                                
                                                                                                                                
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

 
# my_linked_list = LinkedList(4)

# print(my_linked_list.head.value)                                                                                                                        
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
