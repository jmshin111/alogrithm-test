# Definition for singly-linked list.

a=[[1 2],[2 3],[3 4]]

print(a)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

listnode1 = ListNode(1)
listnode1.next = ListNode(2)
listnode1.next.next = ListNode(4)

listnode2 = ListNode(1)
listnode2.next = ListNode(3)
listnode2.next.next = ListNode(4)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = result = ListNode(-1) #startNode
        while l1 or l2:
            if(l1 and l2):
                if(l1.val > l2.val):
                    result.next =l2
                    l2 = l2.next
                else:
                    result.next = l1
                    l1 = l1.next
            elif l1:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next

            result = result.next
        return head.next

linked_list = Solution.mergeTwoLists(Solution,listnode1,listnode2)

while linked_list:
    print(linked_list.val)
    linked_list = linked_list.next
