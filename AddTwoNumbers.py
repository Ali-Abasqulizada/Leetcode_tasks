# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        cur = ans
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            cur.next = ListNode(total % 10)
            cur = cur.next
            carry = total // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next