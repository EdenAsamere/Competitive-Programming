# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(head):
            count = 0
            temp = head
            while temp:
                count += 1
                temp = temp.next
            return count

        dummy = ListNode(0)
        dummy.next = head
        count = helper(head)

        temp2 = dummy
        for i in range(count - n):
            temp2 = temp2.next
        temp2.next = temp2.next.next
        return dummy.next
