# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        head = ListNode(0)
        flag = 0
        l3.val = l1.val + l2.val
        head = l3
        while(l1.next or l2.next):
            tmp = ListNode(0)
            l3.val = l1.val + l2.val + flag
            flag = 0
            if l3.val >= 10:
                l3.val = l3.val % 10
                flag = 1
            if (l1.next):
                l1 = l1.next
            else:
                l1.val = 0
            if (l2.next):
                l2 = l2.next
            else:
                l2.val = 0
            l3.next = tmp
            l3 = l3.next
        l3.val = l1.val + l2.val + flag
        if l3.val >= 10:
            l3.val = l3.val % 10
            flag = 1
            tmp = ListNode(1)
            l3.next = tmp

        return head

        
           


