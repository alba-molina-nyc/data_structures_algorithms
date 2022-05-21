list = [1,2,3,4,5,6,7,8]

# take list and cut it in half && eliminate where the number is not, so we would eliminate l2 && would only then look at l1

l1 = [1,2,3,4]
l2 = [5,6,7,8]


# then you take the list l1 and cut it in half again and do it again, you would eliminate l1_2 until you find the item you were looking for 
l1_1= [1,2]
l1_2= [3,4]

# then you take the list again and split it again and get rid of the list that does not have the number that you are looking for
l1_1_1 = [1]
l1_1_2 = [2]


# count how many steps you had (it took three steps to find that number)

# 2^3 = 8

# very flat, ot the best but very good