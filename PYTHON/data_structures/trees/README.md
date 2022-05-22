# Trees

- A tree is a linked list

- A linked list is just a tree that does not fork
- Trees do not have to be binary, you can have them point to as many nodes as you want including infinity nodes

# Important Tree Terminology

### Full Tree- Every node in the tree points to zero (no node) or two nodes

Ex: if you have a binary tree that has a node that only points to one other node then that tree is not full

It will only be full if it pointed to NO node or TWO nodes

### Perfect Tree- any level of the tree that has any nodes is completely filled all the way across

Ex:if you have a binary tree then every single layer of that tree must point to two other nodes

If it only points to one then it is not a PERFECT tree

### Complete Tree- When you fill the tree from left to right with no gaps

### Parent VS Child node

Ex: when looking at the example in trees.py

The 4 is the parent of 3 and 23

23 and 3 are children of 4

{
"value": 4,
"left": {
"value": 3,
"left": None,
"right": None
},
"right": {
"value": 23,
"left": None,
"right": None
},
}

- Every node can only have one parent

A child node can also have children

A child node can also NOT have children, they are called LEAF
