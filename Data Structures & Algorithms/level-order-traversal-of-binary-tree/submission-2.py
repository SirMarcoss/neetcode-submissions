# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        queue = deque()
        if root:
            queue.append(root)

        while queue:
            lis = []

            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                lis.append(node.val)
            
            res.append(lis)
        return res 
        







# TEST

# First iteration:
# queue : [1]
# queue: []
# list [1]
# queue : [[2], [3]]
# res: [[1]]

# Second iteration:
# queue: [3]
# list: [2]
# queue: [3,4,5]

# third iteration
# queue: [4,5]
# list [2,3]





        