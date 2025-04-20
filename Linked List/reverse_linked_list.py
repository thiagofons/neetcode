# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    previous_node, current_node = None, head
    
    while current_node != None:
      next_node = current_node.next

      current_node.next = previous_node
      previous_node = current_node
      current_node = next_node

    return previous_node



    
  
solution = Solution()

d = ListNode(3, None)
c = ListNode(2, d)
b = ListNode(1, c)
a = ListNode(0, b)

head = a

reversed = solution.reverseList(head)

actual = reversed

while actual != None:
  print(actual.val)
  actual = actual.next

