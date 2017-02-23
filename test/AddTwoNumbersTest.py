import unittest
import AddTwoNumbers


class MyTestCase(unittest.TestCase):
    def test_copylist(self):
        test=AddTwoNumbers.Solution()
        head = AddTwoNumbers.ListNode(1)
        src = AddTwoNumbers.ListNode(2)
        src.next = AddTwoNumbers.ListNode(3)
        list = test.copyList(head, src)

        for i in range(1, 4):
            self.assertEqual(i, list.val)
            list = list.next

    def test_addTwoNumbers(self):
        test = AddTwoNumbers.Solution()
        add1 = AddTwoNumbers.ListNode(2)
        add1.next = AddTwoNumbers.ListNode(4)
        add1.next.next = AddTwoNumbers.ListNode(3)
        add2 = AddTwoNumbers.ListNode(5)
        add2.next = AddTwoNumbers.ListNode(6)
        add2.next.next = AddTwoNumbers.ListNode(4)
        list = test.addTwoNumbers(add1, add2)
        self.assertEqual(list.val, 7)
        self.assertEqual(list.next.val, 0)
        self.assertEqual(list.next.next.val, 8)

if __name__ == '__main__':
    unittest.main()
