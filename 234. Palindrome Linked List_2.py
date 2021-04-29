#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1->2->2->1
#listnode = None
listnode = ListNode(1)
listnode.next = ListNode(2)
#listnode.next.next = ListNode(2)
#listnode.next.next.next = ListNode(1)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        result = False
        odd = False
        index_x_1 = head
        index_x_2 = head
        stack = []
        if not head or not head.next:
            return True
        while head:
            if index_x_1.next:
                stack.append(index_x_1.val)
                index_x_1 = index_x_1.next


            if index_x_2.next:
                index_x_2 = index_x_2.next
            else:
                odd = True
                break

            if index_x_2.next:
                index_x_2 = index_x_2.next
            else:
                break
        if odd:
            stack.pop()
        while index_x_1:
            if(stack.pop() != index_x_1.val):
                return False
            index_x_1 = index_x_1.next

        return True

print(Solution.isPalindrome(Solution,listnode))

