# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n +=1
            if n == k:
                return cur.val
            cur = cur.right

# instead of using the in-order traversal, we should use this iterative DFS.
# in the first case, we would use an array that, in the worse case, contains N values --> time/ space complexity = O(N)
# using iterative DFS the time complexity is O(H + k) --> H is the high of the tree. when we are at NULL, we only have to
# iterate as long as n == k. best case: O(H + 1) --> O(H)
# worste case: O(H + N) --> O(N)