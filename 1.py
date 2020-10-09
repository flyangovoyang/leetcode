class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        (easy)利用链表做加法，数字是倒序表示的，每个结点只包含一个数字。
        """
        mem = 0
        p1, p2 = l1, l2
        l3 = ListNode()
        p3 = l3
        while p1 and p2:
            cur = p1.val + p2.val + mem
            mem = cur//10
            cur = cur%10
            p3.next = ListNode(cur)
            p3 = p3.next
            p1 = p1.next
            p2 = p2.next
        while p1:
            cur = p1.val + mem
            mem = cur//10
            cur = cur%10
            p3.next = ListNode(cur)
            p3 = p3.next
            p1 = p1.next
        while p2:
            cur = p2.val + mem
            mem = cur//10
            cur = cur%10
            p3.next = ListNode(cur)
            p3 = p3.next
            p2 = p2.next
        if mem != 0:
            p3.next = ListNode(mem)
            p3 = p3.next
        return l3.next
