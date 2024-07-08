# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        ans = []
        def find(node):
            if not node:
                return
            find(node.left)
            ans.append(node.val)
            find(node.right)
        find(root)
        return ans