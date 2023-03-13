def preorder_traverse(node):
    if node is None:
        return []
    return ([node.val] +
            preorder_traverse(node.left) +
            preorder_traverse(node.right))
