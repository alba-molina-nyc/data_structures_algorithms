# Trees [Binary]

- A tree is a linked list

- A linked list is just a tree that does not fork
- Trees do not have to be binary, you can have them point to as many nodes as you want including infinity nodes

# Important Tree Terminology

### Full Tree

Every node in the tree points to zero (no node) or two nodes

- Ex: if you have a binary tree that has a node that only points to one other node then that tree is not full

- It will only be full if it pointed to NO node or TWO nodes

### Perfect Tree

- any level of the tree that has any nodes is completely filled all the way across

- Ex:if you have a binary tree then every single layer of that tree must point to two other nodes

- If it only points to one then it is not a PERFECT tree

### Complete Tree

- When you fill the tree from left to right with no gaps

### Parent VS Child node

- Ex: when looking at the example in trees.py

- The 4 is the parent of 3 and 23

- 23 and 3 are children of 4

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

- A child node can also have children

- A child node can also NOT have children, they are called LEAF

### Leaf

- a child node that does not have children

### Binary search trees the nodes have to be laid out in a particular way:

- if the number you are adding is greater than it will go on the right (you will always start at the top)
- if the number you are adding is less than then it will go to the left (you will always start at the top)

# Binary Search Tree [Insertion]

1. compare the node adding to the root

   - if the node is greater than then to the RIGHT
   - if the node is less than then go to the LEFT

2. You are going to now be one below of the root and in the direction that you decided based on steps 1 and 2 using the [temp variable]

   - if the direction you are going is NONE then add the node
   - if the direction you are going is NOT None then are you going left or right like we did in step 1
     - notice that we did the above line of code twice, so it should be inside of a loop AND because we DO NOT KNOW the amount of times we are going to be iterating through the tree it CAN'T be a for loop.
     - It has to be a WHILE LOOP

3. Add two variables [temp] and [root]

   - we already declared root but we were iterating through the tree [moving down] in order to keep track of us iterating through the tree we need to add another variable TEMP
   - temp and root will be declared before we ever get to that while loop
     - [the equivalent of this with a LL would be HEAD]

4. Take account of other edge cases
   - when root is empty, we do not need to go through the while loop, we do not even need the temp variable
   - when the node you are adding in the tree is equal to a node that exists inside the tree i.e.) adding num 76 but there is already a 76 inside the tree
     - you cannot have duplicates, so you need to return FALSE

# Binary Search Tree [Contains]

1. need variables that we need to traverse to through the tree [temp] and also need the variable [root] which will stay at the root

   - you need to start by setting the temp value equal to the root
     - [remember that temp is the variable you are going to be using to iterate through]

2. Compare the node you are searching for in the tree to the root node
   - if the node you are looking for is greater than the root then go RIGHT
   - if the node you are looking for is less than the root then go LEFT
   - if the node you are looking for is equal to temp then return TRUE because it means you have found it
     - at this point you will exit the while loop because you found it
   - if you ever hit None then that means that the node you are looking for is not in the tree so you need to return FALSE
     - at this point you will exit the while loop because the node you are looking for does not exist inside the tree
3. You are going to now be one below of the root and in the direction that you decided based on steps 1 and 2 using the [temp variable]

4. Take account of all of the edge cases i.e.) if the root is empty
