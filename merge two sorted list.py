# A single node of a singly linked list
import sys
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


def mergeTwoSortedList(linked_list1, linked_list2):
    min_data = sys.maxsize
    result_linked_list = LinkedList()
    result_linked_list.end = result_linked_list.head = Node('start')

    while linked_list1 or linked_list2:

      if not linked_list1:
        result_linked_list.add(Node(linked_list2.data))
        linked_list2 = linked_list2.next

      if not linked_list2:
        result_linked_list.add(Node(linked_list1.data))
        linked_list1 = linked_list1.next


      if int(linked_list1.data) < int(linked_list2.data):
        result_linked_list.add(Node(linked_list1.data))
        linked_list1 = linked_list1.next
      else:
        result_linked_list.add(Node(linked_list2.data))
        linked_list2 = linked_list2.next


    return result_linked_list


linked_list = LinkedList()
linked_list.end = linked_list.head = Node(1)
linked_list.add(Node(2))
linked_list.add(Node(4))

linked_list2 = LinkedList()
linked_list2.end = linked_list2.head = Node(1)
linked_list2.add(Node(3))
linked_list2.add(Node(4))

start_time = timeit.default_timer()
print(mergeTwoSortedList(linked_list.head, linked_list2.head))
terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))
