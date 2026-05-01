# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode()
        dummy.next = head
        curr2 = dummy
        N = 0

        while curr:
            N += 1
            curr = curr.next
        print(N)

    
        rIdx = N-n

        for i in range(rIdx):
            curr2 = curr2.next
        print(curr2.val)
        if curr2.next:
            curr2.next = curr2.next.next
        
        return dummy.next