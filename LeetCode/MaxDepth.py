# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaxDepth:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))


maxDepth = MaxDepth()
left = TreeNode(1)
right = TreeNode(2)
root = TreeNode(0,left, right)

depth = maxDepth.maxDepth(root)
print(depth)
