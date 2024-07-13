# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        check = {}
        def find(y, x, node):
            if not node:
                return
            find(y - 1, x + 1, node.left)
            find(y + 1, x + 1, node.right)
            if (y, x) not in check:
                check[(y, x)] = []
            check[(y, x)].append(node.val)
        find(0, 0, root)
        ans = []
        prev = float("-inf")
        for key, value in sorted(check.items()):
            if key[0] != prev:
                ans.append([])
            ans[-1].extend(sorted(value))
            prev = key[0]
        return ans