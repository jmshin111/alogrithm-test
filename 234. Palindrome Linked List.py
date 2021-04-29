#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1->2->2->1

listnode = ListNode(1)
listnode.next = ListNode(0)
listnode.next.next = ListNode(0)
#listnode.next.next.next = ListNode(1)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        result = False
        index = head
        total_count = 0
        while index:
            total_count += 1
            index = index.next
        index = head
        current_count = 0
        stack = []
        print( round(total_count/2))
        while index:
            if current_count< total_count/2:
                stack.append(index.val)
            else:
                if(index.val != stack.pop()):
                    return False
            current_count += 1
            index = index.next
            if ((total_count) % 2 == 1 and (current_count) == int(total_count / 2)):
                current_count += 1
                index = index.next
                continue
        return True

print(Solution.isPalindrome(Solution,listnode))

