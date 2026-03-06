"""
In the ancient Library of Alexandria, a temporal rift has scattered several important scrolls across different rooms. 
You are given a dictionary library_catalog that maps room names to the number of scrolls that room should have and a 
second dictionary actual_distribution that maps room names to the number of scrolls found in that room after the temporal rift.

Write a function analyze_library() that determines if any room has more or fewer scrolls than it should. The function 
should return a dictionary where the keys are the room names and the values are the differences in the number of scrolls 
(actual number of scrolls - expected number of scrolls). You must loop over the dictionaries to compute the differences."""

def analyze_library(library_catalog, actual_distribution):
    dic = {}
    for k in library_catalog.keys():
        dic[k] = actual_distribution[k] - library_catalog[k] 
    
    return dic
            



library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}


#print(analyze_library(library_catalog, actual_distribution)) # {'Room A': 0, 'Room B': -10, 'Room C': 10, 'Room D': 0}

# P 2

def find_common_artifacts(artifacts1, artifacts2):
    pass

artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

#print(find_common_artifacts(artifacts1, artifacts2))

#P3
"""Given a list of strings souvenirs and a integer threshold, declutter your souvenirs by writing a function
declutter() return a list of souvenirs whose frequencies are below the threshold"""
from collections import Counter

def declutter(souvenirs, threshold):
    dic = {}
    res = []
    for s in souvenirs:
        dic[s] = dic.get(s, 0) + 1
    
    for s in souvenirs:
        if dic[s] < threshold:
            res.append(s)
    return res

souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"] # ["alien egg", "map", "map", "statue"]
threshold1 = 3

souvenirs2 = ["postcard", "postcard", "postcard", "sword"] # ['sword']
threshold2 = 2
#print(declutter(souvenirs1, threshold1))
#print(declutter(souvenirs2, threshold2))

#P 4
def num_of_time_portals(portals, destination):
    # make pairs and check each pair if it matches to destination
    count = 0
    for i in range(len(portals)):
        for j in range(i+1, len(portals)):
            if portals[i] + portals[j] == destination:
                count +=1
            if portals[j] + portals[i] == destination:
                count +=1
            

    return count


portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

#print(num_of_time_portals(portals1, destination1))
#print(num_of_time_portals(portals2, destination2))
#print(num_of_time_portals(portals3, destination3))


# P 5

# P 6

# =========
# P 4
# I need to remove 1 char so freq of all chars is same, if so - True, else False

from collections import Counter

def can_make_balanced(code):
    freq = Counter(code)
    freq_count = Counter(freq.values())


    if len(freq_count) > 2:
        return False
    if len(freq_count) == 1:
        f, c = list(freq_count.items())[0]
        return f == 1

    (f1, c1), (f2, c2) = freq_count.items()

    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        return True

    if abs(f1 - f2) == 1 and (c1 == 1 or c2 == 1):
        return True

    return False
    
    

    


code1 = "arghh"
code2 = "haha"

#print(can_make_balanced(code1)) 
#print(can_make_balanced(code2)) 

#p2 set 1
def can_trust_message(message):
    my_set = set()
    for c in message:
        if c != ' ':
            my_set.add(c)
    return len(my_set) == 26

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

#print(can_trust_message(message1))
#print(can_trust_message(message2))

#P3 s1
# Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.
def find_duplicate_chests(chests):
    dic = {}
    res = []
    for c in chests:
        dic[c] = dic.get(c, 0) + 1
    for k, v in dic.items():
        if v == 2:
            res.append(k)
    return res


chests1 = [4, 3, 2, 7, 8, 2, 3, 1] # [2, 3]
chests2 = [1, 1, 2] # [1]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))