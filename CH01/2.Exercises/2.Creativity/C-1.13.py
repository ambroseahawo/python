"""Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing."""

# note;- Linked List is a linear collection of data elements whose order
# is not given by their physical placement in memory

list_of_integers = [6,3,4,6]
reversed_lst = [6,4,3,6]

# Given a pointer to the head node of a linked list, we need to reverse the list
# by changing the links between nodes.

# 1. Iterative Method

"""
1. Initialize three pointers prev as NULL, curr as head, and next as NULL.
2. Iterate through the linked list. In loop, do following.
    - Before changing next of current,
    - store next node
        next = curr->next
    - Now change next of current
    - This is where actual reversing happens
        curr->next = prev
    - Move prev and curr one step forward
        prev = curr
        curr = next
"""

# 2 Recursive Method

"""
1. Divide the list in two parts - first node and rest of the linked list.
2. Call Reverse for the rest of the linked list.
3. Link rest to first
4. Fix head pointer
"""
