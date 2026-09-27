# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSame(root, subRoot):
            return True
        while root.left or root.right:
            if self.isSame(root.right, subRoot) or self.isSame(root.left, subRoot):
                return True
            if root.right:
                root = root.right
            else:
                root = root.left
        return False

    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p or q):
            return True
        if not (p and q):
            return False
        if (p.val != q.val):
            return False
        L = self.isSame(p.left, q.left)
        R = self.isSame(p.right, q.right)
        if L and R:
            return True
        else:
            return False