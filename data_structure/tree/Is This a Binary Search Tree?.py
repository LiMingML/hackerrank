""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    def helper(node, minimum, maximum):
        # Base case.
        if node is None:
            return True

        if node.data <= minimum or node.data >= maximum:
            return False

        return helper(node.left, minimum, node.data) and helper(node.right, node.data, maximum)

    return helper(root, -float('inf'), float('inf'))