# Main function: reverse between left and right
def reverse_between(head, left, right):
    if not head or left == right:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy

    # Step 1: Move prev to the node before `left`
    for _ in range(left - 1):
        prev = prev.next

    # Step 2: Reverse the sublist
    curr = prev.next
    prev_sublist = None
    for _ in range(right - left + 1):
        next_node = curr.next
        curr.next = prev_sublist
        prev_sublist = curr
        curr = next_node

    # Step 3: Reconnect
    tail = prev.next         # tail is the old start of the sublist (now the end)
    tail.next = curr         # connect reversed tail to node after `right`
    prev.next = prev_sublist # connect node before `left` to new head of sublist

    return dummy.next