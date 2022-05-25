# Linked List

- no index
- all nodes are spread out
- you have HEAD points to first item
- you have TAIL points to last item
- each node is connected to the next node
- in the example below the 11 is connect to the 3, the 3 is connected to 23, the 23 is connect to the 7, the 7 is connected to the 4

ex:

LL = [11, 3, 23, 7, 4]

- you need to set two pointers one at the HEAD and one at the TAIL

# Node && LL under the hood

The digits or the nodes are essentially a dictionary (you cannot use the same syntax as dictionary to access it but it is good to think about it like that)

- so the node contains a VALUE and a NEXT

ex:

LL = [11, 3, 23, 7, 4]

- head = {
  "value": 11, "next" { "value: 3, "next" { "value": 23, "next" {"value": 7, "next" {"value": 4, "next": None
  }}}}}

  - head['next']['next']['value'] -- this is how you would access
    print(ll.head.next.next.value)

# Cycles in LL

- a cycle exists in a LL if SAME node can be reached by continously following next pointer
- if SAME node cannot be reached then it is NULL or NONE and therefore NOT a cycle

# Techniques to Figure out Cycles in LL

## 1. Fast and slow in LL to figure out Cycles

- Initialize fast pointer and slow pointer at head
- while loop (fast != None first then fast.next != None)
  - move slow one point
  - move fast one point
- when fast and slow meet we detected a cycle (if fast == slow return True)
- if fast and slow do not ever meet then return False

## 2 Hash Sets

Hash Sets to keep track of visited or duplicate items in LL

- initialize empty hash set
- initialize a pointer to the first node in the list
- set up a while loop
  -(while loops stop when a condition has been met) in this case if the pointer is not Null
- setup if statement we are traversing through through the LL and checking if the node we have our current pointer at has been visited
  - return statement
    - that needs to be returned if the if statement has been satisfied
  - else statement node NOT visited
    - if node not visited then add it to the visited set
- move pointer over by one to the next node
