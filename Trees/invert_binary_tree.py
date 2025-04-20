
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root == None:
      return
    
    aux = root.left
    root.left = root.right
    root.right = aux

    self.invertTree(root.left)
    self.invertTree(root.right)

    return root
    

# Helper function to create a binary tree from a list
def create_binary_tree(values):
  if not values:
    return None
  nodes = [TreeNode(val) if val is not None else None for val in values]
  for i in range(len(nodes)):
    if nodes[i] is not None:
      if 2 * i + 1 < len(nodes):
        nodes[i].left = nodes[2 * i + 1]
      if 2 * i + 2 < len(nodes):
        nodes[i].right = nodes[2 * i + 2]
  return nodes[0]

# Create the binary tree
root = create_binary_tree([1, 2, 3, 4, 5, 6, 7])

# Helper function to print the binary tree from the side
def print_tree(node, level=0, prefix="Root: "):
  if node is not None:
    print_tree(node.right, level + 1, "R---- ")
    print(" " * (4 * level) + prefix + str(node.val))
    print_tree(node.left, level + 1, "L---- ")

# Print the binary tree

solution = Solution()


tree = solution.invertTree(root)
print_tree(tree)



