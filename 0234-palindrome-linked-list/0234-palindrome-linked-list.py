# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        a = []
        cur = head
        while cur:
          a.append(cur.val)
          cur = cur.next 

        return a == a[::-1]
       