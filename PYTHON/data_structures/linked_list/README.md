# Linked List

- each node is connected to the next node
- in the example below the 11 is connect to the 3, the 3 is connected to 23, the 23 is connect to the 7, the 7 is connected to the 4

ex:

LL = [11, 3, 23, 7, 4]

- you need to set two pointers one at the HEAD and one at the TAIL

# Node && LL under the hood

The digits or the nodes are essentially a dictionary (you cannot use the same syntax as dictionary to access it but it is good to think about it like that)

ex:

LL = [11, 3, 23, 7, 4]

- head = {
  "value": 11, "next" { "value: 3, "next" { "value": 23, "next" {"value": 7, "next" {"value": 4, "next": None
  }}}}}

  - head['next']['next']['value'] -- this is how you would access
    print(ll.head.next.next.value)
