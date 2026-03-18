#P1
#from collections import queue
#def blueprint_approval(blueprints):
    

#print(blueprint_approval([3, 5, 2, 1, 4])) 
#print(blueprint_approval([7, 4, 6, 2, 5]))
#[1, 2, 3, 4, 5]
#[2, 4, 5, 6, 7]

def build_skyscrapers(floors):
    buildings = 1
    for i in range(len(floors)-1):
        if floors[i+1] > floors[i]:
            buildings+=1
    return buildings


#print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9]))
# 1  1 1 1

#print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
# 7 + 7 =14 
#print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

#P3
def max_corridor_area(segments):
    l,r =0, len(segments)-1
    max_a = 0
    while l< r:
        h = min(segments[l], segments[r])
        w = r-l
        max_a = max(max_a, h*w)
        if segments[l+1] > segments[r-1]:
            l+=1
        else:
            r-=1
    return max_a


#print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) #49
#print(max_corridor_area([1, 1])) #1

def min_swaps(s):
    count = 0

    for c in s:
        if c == '[':
            count += 1
            if count > 0:
                count -=1

    return count

print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]")) 