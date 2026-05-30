class ListNode:
    def __init__(self , key ):
        self.val = key
        self.next = None
class MyHashSet:

    def __init__(self):
        self.set = [ListNode(-1) for i in range(10 ** 4)]

    def add(self, key: int) -> None:
        hash_index = key % len(self.set)
        head = self.set[hash_index]
        temp = head
        while(temp and temp.next):
            if temp.next.val == key:
                return 
            temp = temp.next
        temp.next = ListNode(key)
        return

    def remove(self, key: int) -> None:
        hash_index = key % len(self.set)
        head = self.set[hash_index]
        temp = head
        while(temp and temp.next):
            if temp.next.val == key:
                temp.next = temp.next.next 
            temp = temp.next
        return

    def contains(self, key: int) -> bool:
        hash_index = key % len(self.set)
        head = self.set[hash_index]
        temp = head
        while(temp and temp.next):
            if temp.next.val == key:
                return True
            temp = temp.next
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)