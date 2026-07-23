# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while list1 is not None:
            arr.append(list1.val)
            list1 = list1.next
        while list2 is not None:
            arr.append(list2.val)
            list2 = list2.next

        arr.sort()

        res = ListNode(-1)
        current = res

        for i in arr:
            current.next = ListNode(i)
            current = current.next
        return res.next


        