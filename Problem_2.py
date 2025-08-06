# // Time Complexity : O(n)
# // Space Complexity : O(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        curr = head
        last = head

        for i in range(n):
            last = last.next
        if(last is None):
            return head.next
        while(last.next is not None):
            last = last.next
            curr = curr.next

        curr.next = curr.next.next
        return head