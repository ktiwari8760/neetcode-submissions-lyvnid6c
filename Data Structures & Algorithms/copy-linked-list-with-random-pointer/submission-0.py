"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummyNode = Node(-1)
        temp = dummyNode
        temp1 = head
        hashmap = {}

        while(temp1):
            value = temp1.val
            temp.next = Node(value)
            hashmap[temp1] = temp.next
            temp = temp.next
            temp1 = temp1.next
        
        temp1 = head
        temp = dummyNode.next

        while(temp1):
            if temp1.random:
                temp.random = hashmap[temp1.random]
            else:
                temp.random = None
            temp = temp.next
            temp1 = temp1.next
        return dummyNode.next


