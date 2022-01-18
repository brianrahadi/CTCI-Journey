# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list

from linked_list import LinkedList


## this is using a space to use seen O(n) time and O(n) space
def remove_dupes_1(ll: LinkedList) -> LinkedList:
  prev = None 
  curr = ll.head
  
  seen = set()

  while curr:
    if curr.value in seen:
      prev.next = curr.next
    else:
      seen.add(curr.value)
      prev = curr
    curr = curr.next
  ll.tail = prev
  return ll

## this is not using space, but it is O(n^2) in time
def remove_dupes_2(ll: LinkedList) -> LinkedList:
  runner = curr = ll.head
  while curr:
    runner = curr
    while runner.next:
      if runner.next.value == curr.value:
        runner.next = runner.next.next
      else:
        runner = runner.next
  ll.tail = runner
  return ll

## for the first one, we use a set to check if values are already seen. if yes, we then 'delete' the current node by having the next of previous to next of current. if not, just add the value to seen and set prev to current node. don't forget to increase curr after that. at the end of loop, set tail of ll to prev

## for the second one, we use a runner that keeps track of the value of current node. this use the same idea but it is in-place, thus costing O(n^2) in time