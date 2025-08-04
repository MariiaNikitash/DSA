"""
(2 + 3 + 4) * (4 + 5) + 1 + 1

`2 3 + 4 5 +    *`
 # Out: int
 # edge cases:
 if empy - return 0
 if just 1 number: return number
 
 
 2 3 4 + + 4 5 + * 1 1 + +
 
 2 3 4 + + 
 
 [2, 7] + [9]
 
     # append to stack until we see +,-,* or /
    2,3 
    # we pop from stack
    
    # perform operation 
    
    # stack = [ 5, 4, 5 ]
    
    # operand +
    # pop -> 5
    # pop -> 4
    # 4 + 5 = 
    # stack = [5]
    
    
    # pop 2 + 2 + 2 + 2
    # 
    
    # stack = 5 9
 
"""


# postfix("2 3 +")
# postfix("23+")
def postfix(s):
    if not s:
        return 0
    # string.split("character to split on, if any")
    list_from_str = s.split(' ') # ["2", "3", "+"]
    stack = []
    operand = set('+', '-', '*', '/')
    for char in list_from_str: # ["2", "3", "+"]
        if char not in operand:
            stack.append(char) 
        if char == '+':
            # .pop() automatically removes the last element, .pop(index)
            subProblem = int(stack.pop()) + int(stack.pop())
            stack.append(subProblem) 
        elif char == '-':
            subProblem = int(stack.pop()) - int(stack.pop())
            stack.append(subProblem)
        elif char == '*':
            subProblem = int(stack.pop()) * int(stack.pop())
            stack.append(subProblem)
        elif char == '/':
            subProblem = int(stack.pop()) / int(stack.pop())
            stack.append(subProblem)
            
        
     
            
    # stack = [5]
    return stack[0]
            
# stack = [2, 3]
        


try:
    num  = int(char)
except ValueError:
    # we know its an operand
    # string expressions & eval