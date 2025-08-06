# // Time Complexity : O(n)
# // Space Complexity : O(1)

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if(slow == fast):
                break
        else:
            return None
        
        fast = head
        
        while(True):
            if(slow == fast):
                break
            fast = fast.next
            slow = slow.next

            
        return slow