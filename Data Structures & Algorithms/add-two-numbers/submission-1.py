# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode() # --> result linked list that we have to return


        # 1 --> thid digit is the carry
        # 0  9 + --> l1
        # 0 9 = --> l2
        # 1 8 -> in each node of the linked list we have only a single digit of the addition

        carry = 0
        while l1 or l2 or carry: # if we have a single digit...
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10 # 18 // 10 = 1
            val = val % 10 # 18 % 10 = 8



            #after that we can insert the value inside the new linked list

            node.next = ListNode(val) # [None]-->[8]
            node = node.next 

            # moving the pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next




        