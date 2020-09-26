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


def palindromLinkedList(linked_list) -> bool:


  #데크 자료형 선언
  q: Deque = collections.deque()

  if  not linked_list.head:
    return True

  node = linked_list.head

  while node is not None:
    q.append(node.data)
    node = node.next


  while len(q)>1:
    if q.popleft() != q.pop():
      return False

  return True


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
