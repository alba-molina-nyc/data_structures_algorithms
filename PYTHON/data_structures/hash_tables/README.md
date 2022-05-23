# Hash Tables

the built in hash tables: dictionaries

- they are built of a key value pairs:

{
"nails":1000
}

- with a hash table though, we are going to need a HASH FUNCTION/METHOD && we will perform a hash on the key
- take the key run it through the hash && in addition to getting our key value pair back we also get an ADDRESS where we store that key value pair

## Two characteristics of a hash:

1. it is one way. i.e) take nails above, run it through the hash and get we get the number two as address, we cannot take the two and put it through the hash to have it produce nails
2. Hash is deterministic - AKA for a particular hash function, every time put nails in, we expect to get the number 2 every time

### Even though Python already provides us with a Hash Table{dictionaries}, we will be creating our own

- we will create our own address space by creating a list
- we will create our methods, so in this case, to set an item, we are going to have a key and a value
- we will create our own hash that will use to hash the key
- and the key value pair is going to be a list
- and the hash is going to produce an address
- and at this address in our list, we will put the list with key, value pair in that spot
- and that will create a list within a list

Once you have items in place, you can run a hash, and because the hash is deterministic, you know the address, and so you can go directly to that address

## Collisions

A collision happens when you put a key value pair at an address where there was already a key value pair

### Separate Chaining

- how is that we can do that without overriding the last key value pair?

- the answer: both of these key value pairs exist within a list inside that address (SEPARATE CHAINING)

### Linear Probing

(open addressing)

Is another popular way of dealing with collisions if you already have an existing key value pair, you will go down the list until you find an empty address and then insert the key value there

- makes it so you do not have more than one at any address
