# first build a node using a class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

{
    'value': 4,
    'left': None,
    'right': None
}
# each node needs to have something pointing to it, except the first node, so in a tree you will call it "root", so you have to create the root variable 


# this is the class for our binarysearchtree
class BinarySearchTree:
    def __init__(self):
        self.root = None


my_tree = BinarySearchTree()

print(my_tree.root)


 