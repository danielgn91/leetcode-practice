# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        resHead = res
        carry = 0
        while l1 != None or l2 != None:
            d1 = l1.val if l1 != None else 0
            d2 = l2.val if l2 != None else 0
            r = d1 + d2 + carry
            if r >= 10:
                res.val = r-10
                carry = 1
            else:
                res.val = r
                carry = 0
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            if l1 != None or l2 != None:
                res.next = ListNode()
                res = res.next
        if carry > 0:
            res.next = ListNode(carry)
        return resHead