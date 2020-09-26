# A single node of a singly linked list
import collections
import timeit
from typing import Deque


class Node:
  # constructor
  def __init__(self, data = None):
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
    self.len = self.len+1


# Linked List with a single node


def reverse_rest_List(linked_list) :


  before_node = linked_list

  middle_node = after_node = linked_list.next
  before_node.next = None
  while after_node.next:

    after_node = after_node.next
    middle_node.next = before_node

    before_node = middle_node
    middle_node = after_node

  after_node.next = before_node
  return after_node


linked_list = LinkedList()
linked_list.end = linked_list.head = Node(1)
linked_list.add(Node(2))
linked_list.add(Node(3))
linked_list.add(Node(4))
linked_list.add(Node(5))



start_time = timeit.default_timer()
print(reverse_rest_List(linked_list.head))


terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))
