class Node:
    def __init__(self , key , value):
        self.key , self.value = key , value
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.head , self.tail = Node(0 , 0) , Node(0 , 0)
        self.head.next , self.tail.prev = self.tail , self.head
    def remove(self , node):
        prev , nextnode = node.prev , node.next
        prev.next = nextnode
        nextnode.prev = prev
    
    def insert(self , node):
        prev = self.tail.prev
        next_node = self.tail
        node.prev = prev
        prev.next = node
        node.next = next_node
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            # We will remove the node from the point where it is and add it to last
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key , value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        
