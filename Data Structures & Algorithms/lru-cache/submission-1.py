class Node:
    def __init__(self ,value=-1, next=None , prev=None , key=None):
        self.value = value
        self.next = next
        self.key = key
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.hash = {} # key : Node pair will be stored here
        self.capacity = capacity # This is the maximum capacity of the cache
        self.head = Node()
        self.tail = self.head
    def detach_node(self , node):
        prever = node.prev
        nexter = node.next
        if prever:
            prever.next = nexter
        if nexter:
            nexter.prev = prever
        if node == self.head:
            self.head = nexter
        if node == self.tail:
            self.tail = prever
        node.prev = None
        node.next = None
        return node
    def attach_node(self , node):
        tailer = self.tail
        tailer.next = node
        node.prev = tailer
        self.tail = node
    def get(self, key: int) -> int:
        # Exists in hash or does not exists in hash
        if key in self.hash:
            node = self.hash[key]
            detached_node = self.detach_node(node) # detached from it's place
            attach_node = self.attach_node(detached_node) # attached at tail
            return node.value
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        # Adding the key we will maintain a linked list 
        # Already Exists
        # Does not exists
            # While adding 
                #Full 
                # Not Full
        if key in self.hash:
            node = self.hash[key]
            node.value = value
            node.key = key
            detached_node = self.detach_node(node) # detached from it's place
            attach_node = self.attach_node(detached_node) # attached at tail
        else: 
            while len(self.hash) > self.capacity-1:
                # because we have to insert that one element
                node = self.head.next
                keyer = node.key
                del self.hash[keyer]
                self.detach_node(node)
            newNode = Node(value = value , next = None , prev = None , key = key)
            attach_node = self.attach_node(newNode) # attached at tail
            self.hash[key] = newNode

            
            