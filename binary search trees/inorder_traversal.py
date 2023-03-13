def inorder_traverse(node):
    if node is None:
        return []
    return (inorder_traverse(node.left) +
            [node.val] +
            inorder_traverse(node.right))
