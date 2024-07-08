# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        ans = []
        def find(node, level):
            if not node:
                return
            elif level == len(ans):
                ans.append([])
            ans[level].append(node.val)
            for cnode in node.children:
                find(cnode, level + 1)
        find(root, 0)
        return ans