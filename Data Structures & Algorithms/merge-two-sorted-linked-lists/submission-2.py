# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # dummy = node = ListNode()

        # while list1 and list2:
        #     if list1.val < list2.val:
        #         node.next = list1
        #         list1 = list1.next

        #     else:
        #         node.next = list2
        #         list2 = list2.next

        #     node = node.next

        # node.next = list1 or list2

        # return dummy.next
        
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
