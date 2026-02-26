class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        for val in self.hashset:
            if key == val:
                self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        for val in self.hashset:
            if key == val:
                return True
        return False