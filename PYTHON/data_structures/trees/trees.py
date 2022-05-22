# this is a node inside a BINARY tree
{
    "value": 4,
    "left": None,
    "right": None
}


# this node can point to other nodes

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

# An then the nodes we added (4,23) can point to other nodes

# Trees do not have to be binary, you can have them point to as many nodes as you want including infinity nodes