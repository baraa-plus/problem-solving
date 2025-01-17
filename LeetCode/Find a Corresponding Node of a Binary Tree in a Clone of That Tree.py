# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method - 1 (Breadth First Search):
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned == None:
            return None

        cloned_deque = deque()
        cloned_deque.append(cloned)

        while cloned_deque:
            head = cloned_deque.popleft()
            if head.val == target.val:
                return head
            if head.left:
                cloned_deque.append(head.left)
            if head.right:
                cloned_deque.append(head.right)
              
        return None

# Method - 2 (Depth First Search):
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned == None:
            return None
        if cloned.val == target.val:
            return cloned
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
