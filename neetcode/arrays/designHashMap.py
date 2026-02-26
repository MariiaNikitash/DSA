class MyHashMap:

    def __init__(self):
        self.mapa = []

    def put(self, key: int, value: int) -> None:
        for pair in self.mapa:
            if pair[0] == key:
                pair[1] = value
                return 
        self.mapa.append([key, value])    

    def get(self, key: int) -> int:
        for k, v in self.mapa:
            if key == k :
                return v
        return -1

    def remove(self, key: int) -> None:
        for i, (k, v) in enumerate(self.mapa):
            if k == key:
                self.mapa.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)