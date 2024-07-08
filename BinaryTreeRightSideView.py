# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        ans = []
        def find(node, level):
            if not node:
                return
            elif level == len(ans):
                ans.append(node.val)
            find(node.right, level + 1)
            find(node.left, level + 1)
        find(root, 0)
        return ans