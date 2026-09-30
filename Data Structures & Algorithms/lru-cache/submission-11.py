class DoubleLinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.volume = 0
        self.index = {} # dictionary for O(1) get
        self.head = DoubleLinkedNode(0,0)
        self.end = DoubleLinkedNode(0,0)

        self.head.next = self.end
        self.end.prev = self.head

    def insert(self, node):
        # move the node into the head
        oldHead = self.head.next
        
        oldHead.prev.next = node
        oldHead.prev = node
        node.next = oldHead
        node.prev = self.head
        
    
    def remove(self, node):
        # the volume over capacity, remove the last node
        node.prev.next = node.next
        node.next.prev = node.prev
        

    def get(self, key: int) -> int:
        # it needs a dict to locate the value
        # then move this to the head of the linkedlist
        # print(key, list(self.index.keys()))
        if key in self.index:
            self.remove(self.index[key])
            # then need to move this node into the head
            self.insert(self.index[key])
            return self.index[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # put to head
        # if exceed the volume, remove the least use one
        if key in self.index:
            self.index[key].val = value
            self.remove(self.index[key])
            self.insert(self.index[key])
        else:
            self.index[key] = DoubleLinkedNode(key, value)
            # print("put", key, self.index)
            # check current volume
            if self.volume < self.capacity:
                # could directly put it in the head
                self.volume += 1
                self.insert(self.index[key])
            else:
                del self.index[self.end.prev.key]
                self.remove(self.end.prev)
                self.insert(self.index[key])

        
