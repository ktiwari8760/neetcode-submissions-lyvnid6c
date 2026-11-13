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
        hash = {}  # This stores the mapping of old node to new node
        dummy = Node(-1)
        temp = dummy
        temp1 = head
        while temp1:
            newNode = Node(temp1.val)
            hash[temp1] = newNode
            temp.next = newNode
            temp = temp.next
            temp1 = temp1.next
        dummyhead = dummy.next

        temp1 = head
        while temp1:
            random_node = temp1.random
            replica_random_node = hash[random_node] if random_node else None
            replica_curr_node = hash[temp1]
            replica_curr_node.random = replica_random_node
            temp1 = temp1.next
        return dummyhead

        

