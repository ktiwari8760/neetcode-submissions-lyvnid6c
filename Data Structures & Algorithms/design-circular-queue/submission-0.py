class Node:
    def __init__(self , val):
        self.val = val
        self.next = None
        self.prev = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.counter = 0
        self.head = Node(-1)

    def enQueue(self, value: int) -> bool:
        if self.counter < self.k:
            self.counter += 1
            temp = self.head
            while(temp.next):
                temp = temp.next
            node = Node(value)
            temp.next = node
            node.prev = temp
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.counter > 0:
            self.counter -= 1
            self.head = self.head.next
            return True
        else:
            return False

    def Front(self) -> int:
        return self.head.val

    def Rear(self) -> int:
        temp = self.head
        while(temp.next):
            temp = temp.next
        return temp.val

    def isEmpty(self) -> bool:
        return self.counter == 0

    def isFull(self) -> bool:
        return self.counter == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()