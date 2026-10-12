# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, None)
        # keep track of current node
        # update current to the smaller of where u are in L1 or where u are in  L2
        l1_pointer = list1
        l2_pointer = list2
        curr = dummy
        
        while l1_pointer is not None or l2_pointer is not None:
            if l1_pointer is None:
                curr.next = l2_pointer
                curr = curr.next
                l2_pointer = l2_pointer.next
            elif l2_pointer is None:
                curr.next = l1_pointer
                curr = curr.next
                l1_pointer = l1_pointer.next

            elif l1_pointer.val <= l2_pointer.val:
                curr.next = l1_pointer
                curr = curr.next
                l1_pointer = l1_pointer.next
            else:
                curr.next = l2_pointer
                curr = curr.next
                l2_pointer = l2_pointer.next

          
        if not dummy.next:
            print("returning nothing")
            return list1
        return dummy.next
          
    