'''
Reorder Linked List
Solved 
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
'''






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle, then starting tht mode reverse list then to new list add one from first list one from reversed
        # [0, 1, 2, 3s,   4, 5, 6f]. 
       
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        slow.next = None
        # reverse second half
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        first = head   
        second = prev 
        while second:
            f_next, s_next = first.next, second.next
            first.next = second
            second.next = f_next
            first, second =  f_next, s_next

# time O(n), 
# space )(1)