# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def greatest_node(root: Node):

    if root.value is None:
        self_max = 0
    else:
        self_max = root.value

    if root.left_child is  None:
        left_max = 0
    else: left_max = greatest_node(root.left_child)
    
    if root.right_child is None:
        right_max = 0
    else:
        right_max = greatest_node(root.right_child)
    
    return max(self_max, left_max, right_max)