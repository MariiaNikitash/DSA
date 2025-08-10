'''
Time Complexity of GRaphs is O(N+E)
'''

"""
JFK ----- LAX
|
|
DFW ----- ATL
"""
# No starter code is provided for this problem
flights = {
    'LAX' : ['JFK'],
    'JFK' : ['LAX', 'DFW'],
    'DFW' : ['ATL', 'JFK'],
    'ATL' : ['DFW']
}


#print(list(flights.keys()))
#print(list(flights.values()))
#print(flights["JFK"])


#['JFK', 'LAX', 'DFW', 'ATL']
#[['LAX', 'DFW'], ['JFK'], ['ATL', 'JFK'], ['DFW']]
#['LAX', 'DFW']


# Problem 2
# given adj list [[1,2], [], [0], [2]] if
# direction from i to j if exists j to i ret True else False
def bidirectional_flights(flights):
    for i in range(len(flights)):
         for j in flights[i]:
              if i not in flights[j]:
                   return False
    return True
flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

#print(bidirectional_flights(flights1))
#print(bidirectional_flights(flights2))


def get_direct_flights(flights, source):
    result = []
    for i in range(len(flights[source])): # length of flights of source row
        if flights[source][i] == 1:
            result.append(i)  # ✅ append the destination index
    return result

flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

#print(get_direct_flights(flights, 2))
#print(get_direct_flights(flights, 3))


# Problem 4
# Convert a list representation of Graph to a dict
def get_adj_dict(flights):
    adj_list = {}
    for a,b in flights:
        if a not in adj_list:
            adj_list[a] = []
        if b not in adj_list[a]:
                adj_list[a].append(b)

        if b not in adj_list:
            adj_list[b] = []
        if a not in adj_list[b]:
                adj_list[b].append(a)
            

    return adj_list
flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
#print(get_adj_dict(flights))

# Output :
{
    'Cape Town': ['Addis Ababa', 'Cairo'],
    'Addis Ababa': ['Cape Town', 'Lagos'],
    'Lagos': ['Cairo', 'Addis Ababa'],
    'Cairo': ['Cape Town', 'Nairobi', 'Lagos'],
    'Nairobi': ['Cairo']
}

from collections import defaultdict
# Problem 5
def find_center(terminals):
    graph = defaultdict(list)
    for a, b in terminals:
        graph[a].append(b)
        graph[b].append(a)
    max_key = max(graph, key=lambda k: len(graph[k]))
    return max_key
#terminals1 = [[1,2],[2,3],[4,2]]
#terminals2 = [[1,2],[5,1],[1,3],[1,4]]

#print(find_center(terminals1))
#print(find_center(terminals2))

# OR 
def find_center(terminals):
    count = {}
    
    for u, v in terminals:
        count[u] = count.get(u, 0) + 1
        count[v] = count.get(v, 0) + 1
    
    # The center node is the one with the highest count (appears n-1 times)
    for terminal, c in count.items():
        if c > 1:  # Appears in more than 1 edge, must be the center
            return terminal
        

from collections import deque
# BFS traversal Goal: Return all locations reachable from a given start, including via layovers.
#Output: A list of all reachable destinations, sorted by number of layovers required 
# Problem 6
def get_all_destinations(flights, start):
    q = deque([start])
    visited = set([start])
    res = []
    while q:
        cur = q.popleft()
        res.append(cur)
        for neighbor in flights.get(cur, []):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return res
         

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": []   
}

#print(get_all_destinations(flights, "Beijing")) # ['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 
#'Reykjavik']
#print(get_all_destinations(flights, "Helsinki")) # ['Helsinki', 'Cairo', 'New York', 'Reykjavik']


# Problem 7 DFS Traversal on same flights problem
def get_all_destinations_dfs(flights, start):
    stack = [start]
    visited = set([start])
    res = []
    while stack:
        cur = stack.pop()
        res.append(cur)
        for neighbor in flights.get(cur, []):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return res

#print(get_all_destinations_dfs(flights, "Beijing"))

# OR Recursionvely 
def get_all_destinations_dfs_recurs(flights, start):
    visited = set()
    res = []

    def dfs(node):
        visited.add(node)
        res.append(node)

        # Expand
        for neighbor in flights.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
    dfs(start)
    return res
#print(get_all_destinations_dfs_recurs(flights, "Beijing"))


# Problem 8

def find_itinerary(boarding_passes):
    dic = {}
    all_arrivals = set()
    for dep, arr in boarding_passes:
        dic[dep] = arr
        all_arrivals.add(arr)
    
    start = None
    for dep, arr in boarding_passes:
        if dep not in all_arrivals:
            start = dep
            break
    
    road = []
    while start:
        road.append(start)
        start = dic.get(start)
        
    return road


boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1)) # ['LAX', 'SFO', 'JFK', 'ATL', 'ORD']
#print(find_itinerary(boarding_passes_2)) # ['LHR', 'DFW', 'JFK', 'LAX', 'DXB']
#Example Output:

