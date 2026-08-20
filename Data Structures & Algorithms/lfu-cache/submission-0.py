class Node:
    def __init__(self, key, val, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev
        self.freq = 1

class LinkedList:
    def __init__(self):
        self.left = Node(0, 0)
        self.right = Node(0, 0, nxt=None, prev=self.left)
        self.left.next = self.right
        self.size = 0
    
    def length(self) -> int:
        return self.size
    
    def pop(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.next = node.prev = None
        self.size -= 1
    
    def popLeft(self) -> None:
        if self.length() == 0: return None
        leftNode = self.left.next
        self.pop(leftNode)
        return leftNode
    
    def pushRight(self, node) -> None:
        rPrev = self.right.prev
        rPrev.next = node
        self.right.prev = node
        node.prev, node.next = rPrev, self.right
        self.size += 1
    

class LFUCache:

    def __init__(self, capacity: int):
        self.nodeMap = {} # -> key: Node
        self.freqMap = collections.defaultdict(LinkedList) # -> {"1": LinkedList, "2": LinkedList}
        self.cap = capacity
        self.leastFreq = 0

    def updateCounter(self, node):
        nodeLL = self.freqMap[node.freq]
        nodeLL.pop(node)
        if (self.leastFreq == node.freq and
            nodeLL.length() == 0):
            del self.freqMap[self.leastFreq]
            self.leastFreq += 1
        
        node.freq += 1
        self.freqMap[node.freq].pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap: return -1
        node = self.nodeMap[key]
        self.updateCounter(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return

        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.updateCounter(node)
            return
        
        if len(self.nodeMap) == self.cap:
            lfu = self.freqMap[self.leastFreq]
            node = lfu.popLeft()
            del self.nodeMap[node.key]
        
        newNode = Node(key, value)
        self.leastFreq = 1
        self.freqMap[self.leastFreq].pushRight(newNode)
        self.nodeMap[key] = newNode


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)