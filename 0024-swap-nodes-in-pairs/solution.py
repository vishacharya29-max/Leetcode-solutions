class Solution:
    def swapPairs(self, head):
        # Base case: if list is empty or has only one node, no swap needed
        if not head or not head.next:
            return head
            
        first = head
        second = head.next
        
        # Swapping recursively
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second
