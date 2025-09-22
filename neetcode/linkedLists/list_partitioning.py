'''
Problem Description

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example 1

Input

[1 --> 4 --> 3 --> 2 --> 5 --> 2], x = 3
Output

[1 --> 2 --> 2 --> 4 --> 3 --> 5]
Note that the order 4, 3, 5 is preserved in the second half of the partition.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x: int) -> ListNode:
    # Dummy heads for two lists
    less_head = ListNode(0)
    greater_head = ListNode(0)

    # Pointers to build the lists
    less = less_head
    greater = greater_head

    # Traverse original list
    cur = head
    while cur:
        if cur.val < x:
            less.next = cur   # attach to "less" list
            less = less.next
        else:
            greater.next = cur  # attach to "greater" list
            greater = greater.next
        cur = cur.next

    # End the greater list
    greater.next = None

    # Connect less list with greater list
    less.next = greater_head.next

    return less_head.next