# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def find(node, level):
            if not node:
                return 0
            elif not node.left and not node.right:
                return level
            return max(find(node.left, level + 1), find(node.right, level + 1))
        return find(root, 1)