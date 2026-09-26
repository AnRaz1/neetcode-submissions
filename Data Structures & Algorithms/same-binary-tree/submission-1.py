# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:   
        # base case
        if not (p or q):
            return True
        if not (p and q):
            return False
        if (p.val != q.val):
            return False
        L = self.isSameTree(p.left, q.left)
        R = self.isSameTree(p.right, q.right)
        if (L and R):
                return True
        else:
            return False