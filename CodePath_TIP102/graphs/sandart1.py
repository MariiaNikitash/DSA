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
print(get_adj_dict(flights))

# Output :
{
    'Cape Town': ['Addis Ababa', 'Cairo'],
    'Addis Ababa': ['Cape Town', 'Lagos'],
    'Lagos': ['Cairo', 'Addis Ababa'],
    'Cairo': ['Cape Town', 'Nairobi', 'Lagos'],
    'Nairobi': ['Cairo']
}


# 