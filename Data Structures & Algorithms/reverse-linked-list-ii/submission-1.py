# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(head):
            temp = head
            prev = None
            while temp:
                nexter = temp.next
                temp.next = prev
                prev = temp
                temp = nexter
            return prev , head
        if not head:
            return None
        left_node_prev = None
        right_node_prev = None
        right_node_next = None
        left_node = head
        right_node = head
        i = 1
        while i <= left or i <= right:
            if i < left:
                left_node_prev = left_node
                left_node = left_node.next
            if i < right:
                right_node_prev = right_node
                right_node = right_node.next
            i += 1
        
        # Detach the array and reverse it 

        if left_node_prev:
            left_node_prev.next = None
        if right_node:
            right_node_next = right_node.next
            right_node.next = None
        
        # We reverse the ll and then get the head and tail 
        header , tailer = reverse(left_node)
        if left_node_prev:
            left_node_prev.next = header
        else:
            head = header
        if right_node_next:
            tailer.next = right_node_next
        return head