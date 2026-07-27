# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # DFS --> pre-order algorithm
        # every step we can count how many nodes are there between the initial node and the last one
        # after that we can store the value inside res if the value is greater than res itself
        # return res at the end
        # time complexity: O(N) because we're analyzing every node only once
        # Space complexity: O(N)

        diameter = 0 # --> we will return this value


        def dfs(root):
            nonlocal diameter 

            if not root:
                return 0
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            diameter = max(diameter, left_height + right_height)

            return 1 + max(left_height, right_height)
        
        dfs(root)

        return diameter

            


            


        


        
        