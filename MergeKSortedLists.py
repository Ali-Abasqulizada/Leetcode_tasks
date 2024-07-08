# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        ans = []
        for llist in lists:
            while llist:
                ans.append((llist.val))
                llist = llist.next
        check = ListNode()
        cur = check
        ans.sort()
        for i in ans:
            cur.next = ListNode(i)
            cur = cur.next
        return check.next