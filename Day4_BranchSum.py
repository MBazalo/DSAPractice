class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def branch_sum(root):
    output = []
    add_node(root, 0, output)
    return output


def add_node(node, total, output):
    total += node.value
    if node.left is not None:
        add_node(node.left, total, output)
    if node.right is not None:
        add_node(node.right, total, output)
    if node.right is None and node.left is None:
        output.append(total)
