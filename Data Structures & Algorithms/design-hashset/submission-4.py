class LinkedList:
    def __init__(self, key):
        self.key = key
        self.next: None | LinkedList = None
class MyHashSet:

    def __init__(self):
        self.hashSet = [LinkedList(0) for i in range(10**4)]
        

    def add(self, key: int) -> None:
        cur = self.hashSet[key % len(self.hashSet)]
        while cur.next:
            if (cur.next.key == key):
                return
            cur = cur.next
        cur.next = LinkedList(key)
        

    def remove(self, key: int) -> None:
        cur = self.hashSet[key % len(self.hashSet)]
        while cur.next:
            if (cur.next.key == key):
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        cur = self.hashSet[key % len(self.hashSet)]
        while cur.next:
            if (cur.next.key == key):
                return True
            cur = cur.next
        return False