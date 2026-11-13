class Node:
    def __init__(self , value , next=None):
        self.value = value
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.size >= self.k:
            return False
        else:
            newNode = Node(value)
            self.size += 1
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                self.tail.next = newNode
                self.tail = newNode
            return True
    def deQueue(self) -> bool:
        if self.size > 0:
            node = self.head
            self.head = self.head.next
            node.next = None
            self.size -= 1
            return True
        else:
            return False
        
    def Front(self) -> int:
        if self.size > 0:
            return self.head.value
        else:
            return -1

    def Rear(self) -> int:
        if self.size > 0:
            return self.tail.value
        else:
            return -1
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()