# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # 1. Check if there are at least k nodes remaining
            kth = self.getKth(group_prev, k)
            if not kth:
                break
                
            group_next = kth.next
            
            # 2. Reverse the group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            # 3. Connect reversed group back into the list
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
            
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
