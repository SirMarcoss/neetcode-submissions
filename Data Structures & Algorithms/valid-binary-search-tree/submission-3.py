# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity = O(N) each node is analyzed only once
# Space Complexity = O(N) we're using a queue as an additional data structure in order to resolve this problem

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root, left, right):
            if not root:
                return True

            if not (root.val < right and root.val > left):
                return False
            
            return (valid(root.left, left, root.val) and valid(root.right, root.val, right))
        
        return valid(root, float("-inf"), float("inf"))
            
  