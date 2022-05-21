my_list = [11, 3, 23, 7]

my_list.append(17)
my_list.pop(17)
my_list.pop(0)
my_list.insert(0, 11)

# right end = O(1)
# left end = O(n) because of the indexing that has to happen
# middle = O(n) because the indexing has to be re-indexed
# when looking for an item by the number O(n)
# but when using index O(1) because you can go directly to that index