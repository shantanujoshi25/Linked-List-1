# // Time Complexity : O(n)
# // Space Complexity : O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(currNode,nextNode):
            if(nextNode.next is None):
                nextNode.next = currNode
                return nextNode
            temp = nextNode.next
            nextNode.next = currNode
            return helper(nextNode,temp)
            

        currNode = head
        if(currNode is None or currNode.next is None):
            return currNode
        nextNode = currNode.next
        currNode.next = None
        return helper(currNode,nextNode)
