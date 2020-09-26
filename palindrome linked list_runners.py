# A single node of a singly linked list
import timeit


class Node:
    # constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None
        self.len = 1

    def add(self, node):
        self.end.next = node
        self.end = node
        self.len = self.len + 1


# Linked List with a single node


def palindromLinkedList(linked_list) -> bool:
    rev = None
    slow = fast = linked_list.head

    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and rev.data == slow.data:
        slow, rev = slow.next, rev.next

    return not rev


linked_list = LinkedList()
linked_list.end = linked_list.head = Node(3)
linked_list.add(Node(4))
linked_list.add(Node(5))
linked_list.add(Node(4))
linked_list.add(Node(3))

start_time = timeit.default_timer()
print(palindromLinkedList(linked_list))
terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))
