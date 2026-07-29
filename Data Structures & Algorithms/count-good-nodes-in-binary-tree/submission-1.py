# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# we can use a DFS algorithm to visit all the nodes of the tree.
# Basically, we use the Pre-Order algorithm in order to visit the children nodes and then we can compare
# them with the parent. if the specific child is greater then the parent, we can increment the res variable

# time complexity = O(N) --> each node is visited only once
# Space compexity = O(N)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxVal):

            if not root:
                return 0
            
            res = 1 if root.val >= maxVal else 0
            maxVal = max (maxVal, root.val)
            res += dfs(root.left, maxVal)
            res += dfs(root.right, maxVal)
            return res
        
        return dfs(root, root.val)
        