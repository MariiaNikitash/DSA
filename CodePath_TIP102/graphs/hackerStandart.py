# Has Path 
# Given adj dict see if thres a path from start to destination and return True/False
# DFS Approach :
def has_path(adjacency_dict, start, destination):
    visited = set()
    def dfs(node):
        if node == destination:
            return True
        visited.add(node)
        for neighbor in adjacency_dict.get(node, []):
            if neighbor not in visited and dfs(neighbor):
                return True
        return False
    
    return dfs(start)

# Notes: always use dict.get() to avoid key error!! 
graph = {
    'A': ['B', 'C'],  # A connects to B and C
    'B': ['D'],       # B connects to D
    'C': ['E'],       # C connects to E
    'D': ['F'],       # D connects to F
    'E': [],          # E has no outgoing edges
    'F': []           # F has no outgoing edges
}

print(has_path(graph, 'A', 'B'))


from collections import deque

def has_path_bfs(adjacency_dict, start, destination):
    if start == destination:
        return True
    visited = set([start])
    q = deque([start])
    while q:
        node = q.popleft()
        for nei in adjacency_dict.get(node, []):  # safe lookup
            if nei == destination:
                return True
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
    return False





# Count connected nodes 
def count_connected_components(adjacency_dict):
    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in adjacency_dict.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

    for node in adjacency_dict:
        if node not in visited:
            count += 1       # Found a new component
            dfs(node)        # Visit all nodes in this component

    return count