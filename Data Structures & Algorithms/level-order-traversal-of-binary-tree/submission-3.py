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
        q = deque()

        if root:
            q.append(root)
        
        while q:
            lis = []
            for _ in range(len(q)):
                node = q.popleft()
                lis.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
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





        