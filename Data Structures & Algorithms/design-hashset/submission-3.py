class MyHashSet:

    def __init__(self):
        self.hashSet = []
        

    def add(self, key: int) -> None:
        if (key not in self.hashSet):
            self.hashSet.append(key)
        

    def remove(self, key: int) -> None:
        if (key in self.hashSet):
            self.hashSet.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.hashSet