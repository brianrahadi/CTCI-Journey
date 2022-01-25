from linked_list import LinkedList, LinkedListNode
# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (not first or last) of a singly linked list, given only access to that node

def delete_middle_node(node: LinkedListNode) -> None:
  if (node == None or node.next == None):
    return None # if node is not a node or last node
  next = node.next
  node.value = next.value
  node.next = next.next

# Time Complexity: O(1)
# Space Complexity: O(1)

# The solution is so simple as I realized the input is the to-be deleted node itself. Just make the next node's value to be the value of this node and the next to be the next of the next node.