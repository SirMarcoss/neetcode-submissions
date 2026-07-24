# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        # [1,2,3] --> first Linked List
        # [4,5,6] --> 2nd linked list

        # 1
        #   9 +
        #   9 =
        # 1 0 where 1 is the carry number


        

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
                v1 = l1.val if l1 else 0
                v2 = l2.val if l2 else 0

                val = v1 + v2 + carry
                carry = val // 10 # --> 30 // 10 = 3
                val = val % 10 ## --> 30 % 10 = 0

                cur.next = ListNode(val)
                cur = cur.next
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None

        return dummy.next





        