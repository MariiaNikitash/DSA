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


# Given undiorected graph as a matrix ret True of graph contains cycles, else False
# While doing DFS, we reach a vertex that has already been visited and it’s not the parent of the current vertex.
def has_cycle(adj_matrix):
    n = len(adj_matrix)
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    # Found a back edge to a visited node that's not the parent
                    return True
        return False

    for start in range(n):
        if start not in visited:
            if dfs(start, -1):  # parent = -1 for the first node
                return True
    return False


'''
dfs(matrix, start) should perform a Depth-First Search on a graph represented as an adjacency matrix.

matrix[i][j] == 1 means there is an edge from node i to node j.

start is the node index to begin the search.

It should return a list of all reachable nodes in DFS order.


'''
def dfs(matrix, start):
    visited = set()
    result = []

    def dfs_recursive(node):
        visited.add(node)
        result.append(node)

        n = len(matrix)
        for neighbor in range(n):
            if matrix[node][neighbor] == 1 and neighbor not in visited:
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return result


matrix = [
 [0, 1, 0, 0],
 [1, 0, 1, 1],
 [0, 1, 0, 0],
 [0, 1, 0, 0]
]
start = 0
