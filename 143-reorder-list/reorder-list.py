# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # base cases: no node, 1 node, 2 nodes (only works with 3)
        if not head or not head.next or not head.next.next:
            return head
        
        # find middle of list
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # split it to 2 list of nodes, find the first node of second list
        curr = slow.next

        #split second part off of first part
        slow.next = None

        #reverse the second list
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp


        # head of 2 lists
        back = prev
        front = head

        #interleave
        while back:
            front_tmp = front.next
            back_tmp = back.next
            front.next = back
            back.next = front_tmp
            front = front_tmp
            back = back_tmp
        
        return head