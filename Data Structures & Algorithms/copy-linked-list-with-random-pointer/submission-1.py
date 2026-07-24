"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# space complexity = O(N) --> we're using an hashtable to stored the data of each node
# time complexity = O(2N) --> O(N) two while loops which iterate through each node -> N node where N is the lenght of linked list

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        dictionary = {None: None} 

        while curr:
            if curr.val not in dictionary:
                dictionary[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = dictionary[curr]
            copy.next = dictionary[curr.next]
            copy.random = dictionary[curr.random]
                  
            curr = curr.next

        

        return dictionary[head]
        

        



        