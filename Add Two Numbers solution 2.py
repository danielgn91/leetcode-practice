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
        return self._addTwoNumbersR(l1, l2,0)
    

    def _addTwoNumbersR(self,l1,l2,carry):
        if carry <=0:
            if l1 is None:
                return l2
            if l2 is None:
                return l1
        else:
            if l1 is None:
                return self._addTwoNumbersR(l2, ListNode(carry),0)
            if l2 is None:
                return self._addTwoNumbersR(l1,ListNode(carry),0)
        r = l1.val + l2.val + carry
        res = ListNode()
        if r >= 10:
            res.val = r-10
            res.next = self._addTwoNumbersR(l1.next, l2.next, 1)
        else:
            res.val = r
            res.next = self._addTwoNumbersR(l1.next, l2.next,0)
        return res