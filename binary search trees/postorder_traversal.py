def postorder_traverse(node):
    if node is None:
        return []
    return (postorder_traverse(node.left) +
            postorder_traverse(node.right) +
            [node.val])
