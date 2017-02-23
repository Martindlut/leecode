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
        mid = 0
        head = ListNode(0)
        tail = head

        while True:
            if l1 is None:
                if l2 is None:
                    tail.val = mid
                    mid /= 10
                else:
                    tail.val = mid + l2.val
                    l2 = l2.next
                    mid = tail.val / 10
                    tail.val %= 10
            elif l2 is None:
                tail.val = l1.val + mid
                mid = tail.val / 10
                l1 = l1.next
                tail.val %= 10
            else:
                tail.val = l1.val + l2.val + mid
                mid = tail.val / 10
                l1 = l1.next
                l2 = l2.next
                tail.val %= 10
            if l1 is not None or l2 is not None or mid != 0:
                tail.next = ListNode(0)
                tail = tail.next
            else:
                break
        return head

    def copyList(self, head, source):
        if head is not None:
            hptr = head
            while source is not None:
                hptr.next = ListNode(source.val)
                hptr = hptr.next
                source = source.next
        return head






