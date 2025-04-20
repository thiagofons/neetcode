from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    list = ListNode(next=None)

    while list1 != None and list2 != None:
      if list1 and list1.val < list2.val:
        list.next = ListNode(list1.val, list)
        list = list.next
        list1 = list1.next

      else:
        list.next = ListNode(list2.val, list)
        list = list.next
        list2 = list2.next

      print(list.val)

    return list
  
solution = Solution()

list1 = [1,2,4] 
list2 = [1,3,5]

def to_linked_list(values):
  if not values:
    return None
  head = ListNode(values[0])
  current = head
  for value in values[1:]:
    current.next = ListNode(value)
    current = current.next

  current.next = None  # Ensure the last element points to None

  return head

list1 = to_linked_list([1, 2, 4])
list2 = to_linked_list([1, 3, 5])

newList = solution.mergeTwoLists(list1, list2)

while newList != None:
  print(newList.val)
  newList = newList.next