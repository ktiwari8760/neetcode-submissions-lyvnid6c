# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1 , l2):
            if not l1:
                return l2
            if not l2:
                return l1
            
            dummy = ListNode()
            temp = dummy
            temp1 = l1
            temp2 = l2
            while temp1 and temp2:
                if temp1.val < temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            while temp1:
                temp.next = temp1
                temp = temp.next
                temp1 = temp1.next
            while temp2:
                temp.next = temp2
                temp = temp.next
                temp2 = temp2.next
            return dummy.next
        while len(lists) > 1:
            merged = []

            for i in range(0 , len(lists) , 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None

                merged.append(merge(l1 , l2))
            lists = merged
        return lists[0] if len(lists) == 1 else None
