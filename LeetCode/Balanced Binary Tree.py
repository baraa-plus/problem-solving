# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
            
        def getHeight(root):
            if root == None:
                return 0
            return max(getHeight(root.left), getHeight(root.right)) + 1

        left_height = getHeight(root.left)
        right_height = getHeight(root.right)
        bf = abs(left_height - right_height)
        if bf > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
