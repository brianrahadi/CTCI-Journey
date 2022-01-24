# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list

from linked_list import LinkedList, LinkedListNode;
def kth_to_last(ll: LinkedList, k: int) -> LinkedListNode:
  current = runner = ll.head

  for _ in range(k):
    if not runner:
      return None
    runner = runner.next

  while runner:
    runner = runner.next
    current = current.next
  
  return current

# Time Complexity: O(n)
# Space Complexity: O(1)

# The way to do it seems tricky at first, but once understood, we found a smart solution to this problem. First, we need to find kth to last. If k is 1, then return the last node. If k is equal to linked list's size, then return the first node. We somehow need to find the reverse of that. The reverse of that means we can just use a temporary node (runner in this case). Runner will go next as many as the amount of k's. After that, we will just move runner and current to it's next node as long as runner is not a nullptr or None. The idea revolves around the node that needs to be moved first. It will later on be used as a helper for the current node to find the correct kth to last position.