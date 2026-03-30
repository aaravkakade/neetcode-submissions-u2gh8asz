# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:   

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        while prev:
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1
            head = tmp1
            prev = tmp2

        
            


        

        

        
        

        


