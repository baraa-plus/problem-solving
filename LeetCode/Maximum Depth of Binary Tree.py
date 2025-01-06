# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method - 1 (Depth First Search):
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Method - 2 (Breadth First Search):
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:     
        if root == None:
            return 0
        
        q = deque()
        q.append(root)

        result = 0

        while q:
            result += 1
            for _ in range(len(q)):    
                top = q.popleft()
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)

        return result
