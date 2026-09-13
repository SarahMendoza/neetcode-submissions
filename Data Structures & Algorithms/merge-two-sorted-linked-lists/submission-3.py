# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        sol = ListNode()
        head = sol
        
        while (list1 != None and list2 != None):
            val1 = list1.val
            val2 = list2.val
            
            if (val1 >= val2):
                sol.next = list2
                list2 = list2.next

            else:
                sol.next = list1
                list1 = list1.next

            sol = sol.next

        if list1 != None:
            sol.next = list1

        elif list2 != None:
            sol.next = list2

        return head.next
