# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        res = []

        if root:
            queue.append(root)

        while queue:
            lenqueue = len(queue)
            for i in range(lenqueue):
                node = queue.popleft()

                if i == lenqueue -1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        
        return res

# Time complexity = O(N) --> every node is analyzed only once
# Space Complexity = O(N) --> we're using a queue to stored every value
# of each node

# TEST
# root: [1,2,3,4,null,null,null,5]
# root is not None --> queue[1]
#First Iteration
# node.left not None and node.right not None -->
# res: [3]
# queue: [2,3]
        