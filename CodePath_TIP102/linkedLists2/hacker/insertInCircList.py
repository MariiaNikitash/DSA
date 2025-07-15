#  LeetCode 708. Insert into a Sorted Circular Linked List
def insert_into_sorted_circular_list(head, insert_val):
    new_node = ListNode(insert_val)
    if not head:
        new_node.next = new_node
        return new_node
    cur = head
    while True:
        if cur.val <= insert_val <= cur.next.val:
            break
        
        
        elif cur.val > cur.next.val:
            if insert_val >= cur.val or insert_val <= cur.next.val:
                break
        
        if cur.next == head:
            break        
            
        cur = cur.next
            
    new_node.next = cur.next
    cur.next = new_node
    
    return head