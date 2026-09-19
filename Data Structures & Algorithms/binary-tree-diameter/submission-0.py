# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # global variable to update maximum diameter as needed during traversal
    maxDiameter = 0
    # recursive function that calculates height and updates diameter
    def diameterRecur(self, root: Optional[TreeNode]) -> int:
        global maxDiameter
        if root is None:
            return 0
        # for each node, longest path is sum of left & right subtree heights
        leftHeight = self.diameterRecur(root.left)
        rightHeight = self.diameterRecur(root.right)
        d = leftHeight + rightHeight
        # update diameter
        if d > maxDiameter:
            maxDiameter = d
        # return height of current subtree
        return 1 + max(leftHeight, rightHeight)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global maxDiameter
        maxDiameter = 0
        self.diameterRecur(root)
        return maxDiameter
