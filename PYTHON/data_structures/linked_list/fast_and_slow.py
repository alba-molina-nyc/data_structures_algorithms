
                # INTERSECTION OF TWO LINKED LISTS https://leetcode.com/problems/intersection-of-two-linked-lists/solution/

# initialize hash set
# traverse through first ll and store all the nodes using a while loop, if reach none then you know you reached the end of LL
# add current node you are on to hash set
# move the head node to the next node
# traverse through LL 2 using a while loop, if reach none then you know you reached the end of the list
# then use if statement to check if the node we are on is in our visited hash set , 
# if contains current node we are on we are going to  return headA because thats the point of intersection  node
# keep moving the pointer of headA
# if at end we do not return anything, that means we do not have an intersection node, so return None

                    # INTERSECTION OF TWO LISTS slow / fast - hare vs tortoise solution

# initialize two pointers in each list p1 at headA and p2 at head2
# move one at slow speed then other at fast speed (hare vs tortoise)
# when respective pointer reaches null set/start pointer at other LL 
# when they reach the same spot then you have landed on the intersection point so return the intersection point
# if they reach null then return False