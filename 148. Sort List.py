# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



list = [4,2]
list = [4,2,1]
list = [4,2,1,3,5]
head = ListNode(list[0])
cuurent_node = head

for i in range(0,len(list)):
    if i ==0 :
        continue
    listNode = ListNode(list[i])
    cuurent_node.next = listNode
    cuurent_node = cuurent_node.next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        if not head:
            return None

        if not head.next :
            return head

        one_speed_node = head
        double_speed_node = head
        before_node = None

        while double_speed_node :
            before_node = one_speed_node
            one_speed_node= one_speed_node.next
            if not double_speed_node.next:
                break
            double_speed_node = double_speed_node.next.next

        before_node.next = None

        first_node = self.sortList(self,head)
        second_node =self.sortList(self,one_speed_node)

        if not first_node and not second_node:
            return None
        elif not first_node and second_node:
            return second_node
        elif first_node and not second_node:
            return first_node

        start_node = None
        current_node = None

        if first_node.val < second_node.val:
            start_node = first_node
            current_node = first_node
            first_node = first_node.next

        else:
            start_node = second_node
            current_node = second_node
            second_node = second_node.next

        while first_node or second_node:

            if first_node and not second_node:
                current_node.next = first_node
                break

            if second_node and not first_node:
                current_node.next = second_node
                break

            if first_node.val < second_node.val:
                current_node.next = first_node
                first_node = first_node.next

            else:
                current_node.next = second_node
                second_node = second_node.next

            current_node = current_node.next

        return start_node

node =  Solution.sortList(Solution,head)
while node:
 print(node.val)
 node = node.next
