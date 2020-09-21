# A single node of a singly linked list
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


def palindromLinkedList(num_array : LinkedList) -> bool:


  stack = []

  index = 1
  odd_number_result = False
  half_number =0

  result = True
  if linked_list.len % 2 == 1:
    odd_number_result = True
    half_number = (int)(linked_list.len / 2 + 1)
  else:
    odd_number_result = False
    half_number = (int)(linked_list.len / 2)

  index_linked_list = linked_list.head
  while index_linked_list != None:

    if( odd_number_result and index == half_number ):
      index = index + 1
      index_linked_list = index_linked_list.next
      continue
    elif (index <= half_number):
      stack.append(index_linked_list.data)
    elif (index_linked_list.data != stack.pop()):
      result = False
      break

    index = index+1
    index_linked_list = index_linked_list.next

  return result


linked_list = LinkedList()
linked_list.end = linked_list.head = Node(3)
linked_list.add(Node(4))
linked_list.add(Node(5))
linked_list.add(Node(4))
linked_list.add(Node(3))



print(palindromLinkedList(linked_list))
