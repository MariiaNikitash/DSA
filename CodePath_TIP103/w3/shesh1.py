#P1
def arrange_guest_arrival_order(arrival_pattern):
    res = []
    stack = []
    cur = 1
    for c in arrival_pattern:
        if c == 'I':
            res.append(str(cur))
            cur +=1
            while stack:
                res.append(stack.pop())
        else:
            stack.append(cur)
            cur +=1
    if arrival_pattern[-1] == 'D':
        stack.append(str(cur))
    else:
        res.append(str(cur))
    while stack:
        res.append(stack.pop())

    return res

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD")) 
#P2
from collections import deque
def reveal_attendee_list_in_order(attendees):
    n = len(attendees)
    res = [0] * n
    # make a q for indecies 0-n
    q = deque(range(n))
    attendees.sort()
    for num in attendees:
        idx = q.popleft()
        res[idx] = num

        if q:
            q.append(q.popleft())

    return res



    # 




print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))  

