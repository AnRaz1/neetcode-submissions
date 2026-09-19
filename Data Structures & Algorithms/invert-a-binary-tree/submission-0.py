# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        result = []
        self.invertTree(root.left) # traverse left subtree
        self.invertTree(root.right) # traverse right subtree
        temp = root.left # swap left & right subtrees
        root.left = root.right
        root.right = temp
        result.append(root.val) # add to inverted tree
        return root
