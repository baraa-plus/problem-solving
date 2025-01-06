# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method - 1 (Depth First Search):
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root == None:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

# Method - 2 (Breadth First Search):
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        bfs = deque()
        bfs.append(root)
        while (bfs):
            r = bfs.popleft()
            if (r):
                bfs.append(r.left)
                bfs.append(r.right)
                if (r.val >= low and r.val <= high):
                    result += r.val
        return result
