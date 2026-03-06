# P 1
def find_balanced_subsequence(art_pieces):
    d = {}
    longest = 0
    for a in art_pieces:
        d[a] = d.get(a, 0) + 1
    
    for num in d:
            if num + 1 in d:
                longest = max(longest, d[num] + d[num+1])

    return longest


art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1)) # 5
print(find_balanced_subsequence(art_pieces2)) # 2
print(find_balanced_subsequence(art_pieces3)) # 0

# P 2
def is_authentic_collection(art_pieces):
    # find max value n, n should appear twice, and len of array is n + 1
    # count freqs
    # find max if freq is 
    d = {}
    len_art = len(art_pieces) 
    max_art = max(art_pieces)
    if len_art != max_art+1:
        return False
    for art in art_pieces:
        d[art] = d.get(art, 0) + 1

    if d[max_art] != 2:
        return False
    
    for val in range(1, max_art):
        if d.get(val, 0) !=1:
            return False
    return True

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1,3,3]

#print(is_authentic_collection(collection1))
#print(is_authentic_collection(collection2))
#print(is_authentic_collection(collection3))

# P 3

def organize_exhibition(collection):
    rows= []
    dic = {}
    res = []
    for c in collection:
        dic[c] = dic.get(c, 0) +1

    while dic:
        row = []
        for k in list(dic.keys()):
            if dic[k] >=1:
                row.append(k)
                dic[k] -=1
            else:
                del dic[k]
        res.append(row)
    
    return res


collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))