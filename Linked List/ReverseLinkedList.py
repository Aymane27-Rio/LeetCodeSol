# Link: https://leetcode.com/problems/reverse-linked-list/description

# Given the head of a singly linked list, reverse the list, and return the reversed list's head.


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        prev = None
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev